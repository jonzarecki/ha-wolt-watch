Implementation Spec – “Watch Wolt” Home Assistant Add-on

(Hand this to another AI / engineer; it should contain every detail needed to ship.)

⸻

1. Background & Intent

Jonathan (Tel Aviv, HA power-user) wants a one-click way to get push alerts when a chosen Wolt restaurant flips from closed → open.
Hard requirements:
	•	No per-restaurant entities (keep the instance clean).
	•	Dashboard button triggers everything via a simple form.
	•	Must be HACS-installable so new users can set it up in <2 min.
	•	Leverage his own wolt-sdk for API calls.

Solution: one HACS repo bundling (a) a lightweight integration that exposes a wolt_watch.start service and (b) a custom Lovelace card that collects the form values and fires the service.

⸻

2. High-Level UX
	1.	User clicks the “Watch Wolt” card (from dashboard’s Custom section).
	2.	Card pops a modal (or inline controls):
	•	Slug text field (taizu, mcdonalds-dizengoff, …).
	•	Watch for duration picker (default 2 h).
	•	Notify device dropdown (mobile_app entities).
	3.	Hit Start → toast “Watching Taizu…”.
	4.	The backend polls Wolt every 60 s; on first open it calls notify.mobile_app_xxx.
	5.	Job self-terminates or times out; no HA entities/helpers created.

⸻

3. Tech Stack & Key Decisions

Layer	Choice	Reason
Polling logic	Custom integration (custom_components/wolt_watch)	Removes Pyscript dependency; auto-installs wolt-sdk via manifest.json.
UI	Lovelace card (www/wolt-watch-card.js, LitElement)	Ships with repo, appears under Add Card → Custom.
Packaging	HACS repo with "domains": ["integration","lovelace"]	One install brings both backend & card.
Service schema	slug (str), timeout_m (int, default 30), device (notify entity)	Mirrors card inputs.
Poll interval	60 s (config constant)	Polite to Wolt; easy to tweak.


⸻

4. Repository Layout

hass-wolt-watch/
├─ custom_components/
│  └─ wolt_watch/
│     ├─ __init__.py          # register service, spawn async task
│     ├─ manifest.json        # domain, version, requirements:["wolt-sdk>=0.1.0"]
│     └─ services.yaml        # YAML schema for HA UI
├─ www/
│  └─ wolt-watch-card.js      # LitElement card
├─ hacs.json                  # HACS metadata (see §8)
└─ README.md                  # install badges, docs


⸻

5. Backend Integration (pseudo-code)

# custom_components/wolt_watch/__init__.py
from datetime import timedelta, datetime
import asyncio, logging
from wolt_api import WoltAPI

DOMAIN = "wolt_watch"
SCAN_INTERVAL = timedelta(seconds=60)
_LOGGER = logging.getLogger(__name__)
api = WoltAPI()

async def async_setup(hass, config):
    async def _start(call):
        slug      = call.data["slug"]
        timeout_m = call.data.get("timeout_m", 30)
        timeout_s = timeout_m * 60  # Convert to seconds
        device    = call.data["device"]

        async def worker():
            end = datetime.utcnow().timestamp() + timeout_s
            seen_open = False
            while datetime.utcnow().timestamp() < end:
                try:
                    open_now = await hass.async_add_executor_job(
                        api.is_restaurant_open, slug)
                except Exception as e:
                    _LOGGER.warning("Wolt check failed: %s", e)
                    await asyncio.sleep(90)
                    continue
                if open_now and not seen_open:
                    await hass.services.async_call(
                        *device.split(".", 1),  # domain, service
                        {"message": f"{slug.replace('-',' ').title()} is now OPEN on Wolt!"}
                    )
                    return
                seen_open = open_now
                await asyncio.sleep(SCAN_INTERVAL.total_seconds())

        hass.async_create_task(worker())

    hass.services.async_register(DOMAIN, "start", _start)
    return True

services.yaml

start:
  name: Start Watch
  description: Watch a Wolt restaurant and notify when it opens.
  fields:
    slug:
      required: true
      example: "taizu"
      selector: text
    timeout_s:
      required: false
      default: 7200
      selector: number:
        min: 60
        max: 86400
        unit_of_measurement: seconds
    device:
      required: true
      selector:
        entity:
          domain: notify
          integration: mobile_app


⸻

6. Lovelace Card (key parts)

class WoltWatchCard extends LitElement {
  static properties = { hass:{}, config:{} };

  render() {
    const devices = Object.keys(this.hass.states)
      .filter(e => e.startsWith("notify.mobile_app"));
    return html`
      <ha-card header="Watch Wolt">
        <div class="card-content">
          <ha-textfield label="Slug" id="slug"></ha-textfield>
          <ha-duration-input id="dur" label="Watch for"></ha-duration-input>
          <ha-select label="Device" id="dev">
            ${devices.map(d => html`<mwc-list-item value=${d}>${d}</mwc-list-item>`)}
          </ha-select>
          <mwc-button raised label="Start" @click=${this._run}></mwc-button>
        </div>
      </ha-card>`;
  }
  _run() {
    const slug = this.shadowRoot.getElementById("slug").value.trim();
    const seconds = this.shadowRoot.getElementById("dur").seconds || 7200;
    const device = this.shadowRoot.getElementById("dev").value;
    if (!slug || !device) return;
    this.hass.callService("wolt_watch", "start",
      { slug, timeout_s: seconds, device });
    fireEvent(this, "hass-notification",
      { message: `Watching ${slug}…` });
  }
}
customElements.define("wolt-watch-card", WoltWatchCard);

HACS automatically adds /hacsfiles/wolt-watch-card.js to resources.

⸻

7. README Essentials
	•	Two “My” badges
Install repo:
[![](https://my.home-assistant.io/badges/hacs_repository.svg)](my.home-assistant://hacs?addon_repository_url=https://github.com/yourname/hass-wolt-watch)
Add card:
[![](https://my.home-assistant.io/badges/dashboard.svg)](my.home-assistant://lovelace/default_view?show_add_card&card_type=custom:wolt-watch-card)
	•	Usage GIF or screenshot.
	•	Troubleshooting (rate-limits, slug lookup tips).

⸻

8. HACS Metadata (hacs.json)

{
  "name": "Wolt Watch",
  "content_in_root": false,
  "render_readme": true,
  "domains": ["integration", "lovelace"],
  "country": "ISR",
  "homeassistant": "2024.1.0",
  "zip_release": false
}


⸻

9. Edge Cases & Safeguards
	•	Debounce: don’t send duplicate opens – implemented via seen_open.
	•	API failures: catch exceptions, back-off 90 s.
	•	429 handling (future): inspect status, exponential back-off.
	•	HA restart: current watches vanish (acceptable per requirement).
	•	Timeout default 2 h; enforce min 60 s.

⸻

10. Stretch / Future Ideas
	•	Autocomplete slug search (/search) endpoint in card.
	•	Optional “repeat daily” helpers and blueprint.
	•	Persist last open state to store to reduce first-poll latency.
	•	Multi-restaurant batch watch (array input).

⸻

11. Deliverables Checklist

Item	Done?
Repo scaffold with correct paths	◻︎
manifest.json with wolt-sdk requirement	◻︎
Working integration & service	◻︎
Lovelace card JS (LitElement)	◻︎
hacs.json + tags	◻︎
README with badges, install steps	◻︎
Tested on HA 2025.6+ (core & Container)	◻︎
GitHub release v0.1.0	◻︎


⸻

12. Acceptance Criteria
	1.	Fresh HA instance → Install via HACS badge → restart once.
	2.	“Add Card → Wolt Watch” appears.
	3.	Filling mcdonalds-dizengoff, 1 h, iPhone → Start.
	4.	When venue opens, iPhone receives exactly one push; no HA error logs.
	5.	No new entities in Developer Tools → States.

⸻

Hand this doc to your build agent—it contains every path, file, and schema needed to implement and ship Wolt Watch as a polished HACS package with a single dashboard button UX.