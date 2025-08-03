"""Wolt Watch integration for Home Assistant."""
from __future__ import annotations

from datetime import timedelta, datetime
import asyncio
import logging
from typing import Any

from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import ConfigType
import voluptuous as vol
from homeassistant.helpers import config_validation as cv

from .const import (
    DOMAIN,
    DEFAULT_SCAN_INTERVAL,
    DEFAULT_TIMEOUT_MINUTES,
    BACKOFF_INTERVAL_SECONDS,
    SERVICE_START,
    CONF_SLUG,
    CONF_TIMEOUT_M,
    CONF_DEVICE,
    MIN_TIMEOUT_MINUTES,
    MAX_TIMEOUT_MINUTES,
)

_LOGGER = logging.getLogger(__name__)

# Config schema - allow empty config for out-of-box experience
CONFIG_SCHEMA = vol.Schema({
    vol.Optional(DOMAIN): vol.Schema({})
}, extra=vol.ALLOW_EXTRA)

# Service schema
SERVICE_START_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_SLUG): cv.string,
        vol.Optional(CONF_TIMEOUT_M, default=DEFAULT_TIMEOUT_MINUTES): vol.All(
            vol.Coerce(int), vol.Range(min=MIN_TIMEOUT_MINUTES, max=MAX_TIMEOUT_MINUTES)
        ),
        vol.Required(CONF_DEVICE): cv.string,
    }
)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Wolt Watch integration."""

    async def _start_watch(call: ServiceCall) -> None:
        """Start watching a Wolt restaurant."""
        slug: str = call.data[CONF_SLUG]
        timeout_m: int = call.data.get(CONF_TIMEOUT_M, DEFAULT_TIMEOUT_MINUTES)
        device: str = call.data[CONF_DEVICE]
        
        # Convert minutes to seconds for internal calculations
        timeout_s = timeout_m * 60

        _LOGGER.info("Starting Wolt watch for %s (timeout: %dm/%ds)", slug, timeout_m, timeout_s)

        async def worker() -> None:
            """Worker task to poll Wolt API."""
            try:
                # Import the real Wolt API client
                from wolt_api_mcp import WoltAPI  # pylint: disable=import-outside-toplevel
                api = WoltAPI()
            except ImportError as e:
                _LOGGER.error(
                    "Failed to import Wolt API client: %s. "
                    "Make sure wolt-sdk is installed: pip install git+https://github.com/jonzarecki/wolt-sdk.git", e
                )
                return
            except Exception as e:
                _LOGGER.error("Failed to initialize Wolt API: %s", e)
                return

            end_time = datetime.utcnow().timestamp() + timeout_s
            seen_open = False

            while datetime.utcnow().timestamp() < end_time:
                try:
                    # Call the Wolt API in executor to avoid blocking
                    open_now = await hass.async_add_executor_job(
                        api.is_restaurant_open, slug
                    )

                    if open_now and not seen_open:
                        # Restaurant opened! Send notification
                        restaurant_name = slug.replace("-", " ").title()
                        message = f"{restaurant_name} is now OPEN on Wolt!"

                        # Parse device entity (e.g., "notify.mobile_app_iphone")
                        if "." not in device:
                            _LOGGER.error("Invalid device format: %s", device)
                            return
                        
                        domain, service = device.split(".", 1)

                        await hass.services.async_call(
                            domain,
                            service,
                            {"message": message},
                        )

                        _LOGGER.info("Sent notification: %s", message)
                        return  # Job complete

                    seen_open = open_now

                except Exception as e:
                    _LOGGER.warning("Wolt API check failed for %s: %s", slug, e)
                    # Back off for longer on error
                    await asyncio.sleep(BACKOFF_INTERVAL_SECONDS)
                    continue

                # Normal polling interval
                await asyncio.sleep(DEFAULT_SCAN_INTERVAL.total_seconds())

            _LOGGER.info("Wolt watch timeout reached for %s", slug)

        # Start the worker task
        hass.async_create_task(worker())

    # Register the service
    hass.services.async_register(
        DOMAIN, SERVICE_START, _start_watch, schema=SERVICE_START_SCHEMA
    )

    _LOGGER.info("Wolt Watch integration loaded")
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Wolt Watch from a config entry."""
    # This integration doesn't use config entries yet
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return True