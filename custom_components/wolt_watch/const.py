"""Constants for the Wolt Watch integration."""
from __future__ import annotations

from datetime import timedelta

# Integration domain
DOMAIN = "wolt_watch"

# Default configuration values
DEFAULT_TIMEOUT_MINUTES = 30  # 30 minutes
DEFAULT_SCAN_INTERVAL = timedelta(seconds=60)
BACKOFF_INTERVAL_SECONDS = 90

# Service configuration
SERVICE_START = "start"

# Configuration keys
CONF_SLUG = "slug"
CONF_TIMEOUT_M = "timeout_m"
CONF_DEVICE = "device"

# Validation limits
MIN_TIMEOUT_MINUTES = 1  # 1 minute
MAX_TIMEOUT_MINUTES = 1440  # 24 hours