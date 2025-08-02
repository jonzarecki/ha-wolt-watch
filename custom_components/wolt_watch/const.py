"""Constants for the Wolt Watch integration."""
from __future__ import annotations

from datetime import timedelta

# Integration domain
DOMAIN = "wolt_watch"

# Default configuration values
DEFAULT_TIMEOUT_SECONDS = 7200  # 2 hours
DEFAULT_SCAN_INTERVAL = timedelta(seconds=60)
BACKOFF_INTERVAL_SECONDS = 90

# Service configuration
SERVICE_START = "start"

# Configuration keys
CONF_SLUG = "slug"
CONF_TIMEOUT_S = "timeout_s"
CONF_DEVICE = "device"

# Validation limits
MIN_TIMEOUT_SECONDS = 60
MAX_TIMEOUT_SECONDS = 86400  # 24 hours