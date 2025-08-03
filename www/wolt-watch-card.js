/**
 * Wolt Watch Card for Home Assistant
 * Based on LitElement for modern web components
 */

import {
  LitElement,
  html,
  css,
} from "https://unpkg.com/lit-element@2.4.0/lit-element.js?module";

class WoltWatchCard extends LitElement {
  static properties = { 
    hass: {}, 
    config: {} 
  };

  static getConfigElement() {
    return document.createElement("wolt-watch-card-editor");
  }

  static getStubConfig() {
    return {};
  }

  setConfig(config) {
    this.config = config;
  }

  getCardSize() {
    return 3;
  }

  render() {
    if (!this.hass) {
      return html`<ha-card>Loading...</ha-card>`;
    }

    // Get all mobile_app notify entities
    const notifyEntities = Object.keys(this.hass.states)
      .filter(entityId => entityId.startsWith("notify.mobile_app"))
      .sort();

    return html`
      <ha-card header="Watch Wolt Restaurant">
        <div class="card-content">
          <div class="input-group">
            <ha-textfield
              id="slug"
              label="Restaurant Slug"
              placeholder="e.g., taizu, mcdonalds-dizengoff"
              helper-text="Find the restaurant slug from the Wolt URL"
              outlined
              style="width: 100%; margin-bottom: 16px;"
            ></ha-textfield>
          </div>

          <div class="input-group">
            <label class="duration-label">Watch Duration</label>
            <ha-duration-input
              id="duration"
              label="Duration"
              .data=${{ hours: 2, minutes: 0, seconds: 0 }}
              style="width: 100%; margin-bottom: 16px;"
            ></ha-duration-input>
          </div>

          <div class="input-group">
            <ha-select
              id="device"
              label="Notification Device"
              outlined
              style="width: 100%; margin-bottom: 16px;"
            >
              <mwc-list-item value="">Select a device...</mwc-list-item>
              ${notifyEntities.map(entityId => {
                const friendlyName = this.hass.states[entityId]?.attributes?.friendly_name || entityId;
                return html`
                  <mwc-list-item value="${entityId}">
                    ${friendlyName}
                  </mwc-list-item>
                `;
              })}
            </ha-select>
          </div>

          <div class="button-container">
            <mwc-button
              raised
              @click="${this._startWatch}"
              style="width: 100%;"
            >
              <ha-icon icon="mdi:food-takeout-box" slot="icon"></ha-icon>
              Start Watching
            </mwc-button>
          </div>
        </div>
      </ha-card>
    `;
  }

  async _startWatch() {
    const slugElement = this.shadowRoot.getElementById("slug");
    const durationElement = this.shadowRoot.getElementById("duration");
    const deviceElement = this.shadowRoot.getElementById("device");

    const slug = slugElement.value?.trim();
    const device = deviceElement.value;

    if (!slug) {
      this._showError("Please enter a restaurant slug");
      return;
    }

    if (!device) {
      this._showError("Please select a notification device");
      return;
    }

    // Get duration in seconds
    const durationData = durationElement.data || { hours: 2, minutes: 0, seconds: 0 };
    const timeoutSeconds = 
      (durationData.hours || 0) * 3600 + 
      (durationData.minutes || 0) * 60 + 
      (durationData.seconds || 0);

    if (timeoutSeconds < 60) {
      this._showError("Duration must be at least 60 seconds");
      return;
    }

    try {
      // Check if the service exists
      if (!this.hass.services.wolt_watch || !this.hass.services.wolt_watch.start) {
        this._showError("Wolt Watch integration not loaded. Please restart Home Assistant and try again.");
        return;
      }

      // Call the service (convert seconds to minutes)
      const timeoutMinutes = Math.round(timeoutSeconds / 60);
      await this.hass.callService("wolt_watch", "start", {
        slug: slug,
        timeout_m: timeoutMinutes,
        device: device,
      });

      // Show success notification
      this._fireEvent("hass-notification", {
        message: `Now watching ${slug.replace(/-/g, " ").replace(/\b\w/g, l => l.toUpperCase())}...`,
      });

      // Clear form
      slugElement.value = "";
      deviceElement.value = "";
      
    } catch (error) {
      this._showError(`Failed to start watching: ${error.message}`);
    }
  }

  _showError(message) {
    this._fireEvent("hass-notification", {
      message: message,
      level: "error",
    });
  }

  _fireEvent(type, detail) {
    const event = new CustomEvent(type, {
      detail: detail,
      bubbles: true,
      composed: true,
    });
    this.dispatchEvent(event);
  }

  static get styles() {
    return css`
      :host {
        display: block;
      }

      .card-content {
        padding: 16px;
      }

      .input-group {
        margin-bottom: 16px;
      }

      .duration-label {
        display: block;
        font-size: 12px;
        color: var(--secondary-text-color);
        margin-bottom: 4px;
      }

      .button-container {
        margin-top: 16px;
      }

      ha-textfield,
      ha-select,
      ha-duration-input {
        width: 100%;
      }

      mwc-button {
        --mdc-theme-primary: var(--primary-color);
      }

      ha-icon {
        margin-right: 8px;
      }
    `;
  }
}

// Define the custom element
customElements.define("wolt-watch-card", WoltWatchCard);

// Add to the custom cards list for Home Assistant
window.customCards = window.customCards || [];
window.customCards.push({
  type: "wolt-watch-card",
  name: "Wolt Watch Card",
  description: "A card to watch Wolt restaurants and get notifications when they open",
  preview: true,
});

console.info(
  `%c WOLT-WATCH-CARD %c v0.1.0 `,
  "color: orange; font-weight: bold; background: black",
  "color: white; font-weight: bold; background: dimgray"
);