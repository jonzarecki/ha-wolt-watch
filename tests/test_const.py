"""Test Wolt Watch constants."""
from __future__ import annotations

import sys
from pathlib import Path
from datetime import timedelta

# Add the custom_components directory to sys.path for importing
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir / "custom_components"))

# Import the constants directly from the file without going through __init__.py
import importlib.util
spec = importlib.util.spec_from_file_location(
    "const", 
    root_dir / "custom_components" / "wolt_watch" / "const.py"
)
const_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(const_module)

# Extract constants
DOMAIN = const_module.DOMAIN
DEFAULT_TIMEOUT_SECONDS = const_module.DEFAULT_TIMEOUT_SECONDS
DEFAULT_SCAN_INTERVAL = const_module.DEFAULT_SCAN_INTERVAL
BACKOFF_INTERVAL_SECONDS = const_module.BACKOFF_INTERVAL_SECONDS
SERVICE_START = const_module.SERVICE_START
CONF_SLUG = const_module.CONF_SLUG
CONF_TIMEOUT_S = const_module.CONF_TIMEOUT_S
CONF_DEVICE = const_module.CONF_DEVICE
MIN_TIMEOUT_SECONDS = const_module.MIN_TIMEOUT_SECONDS
MAX_TIMEOUT_SECONDS = const_module.MAX_TIMEOUT_SECONDS


def test_domain():
    """Test domain constant."""
    assert DOMAIN == "wolt_watch"
    assert isinstance(DOMAIN, str)


def test_timeout_constants():
    """Test timeout-related constants."""
    assert DEFAULT_TIMEOUT_SECONDS == 7200  # 2 hours
    assert MIN_TIMEOUT_SECONDS == 60  # 1 minute
    assert MAX_TIMEOUT_SECONDS == 86400  # 24 hours
    
    # Validate the range makes sense
    assert MIN_TIMEOUT_SECONDS < DEFAULT_TIMEOUT_SECONDS < MAX_TIMEOUT_SECONDS


def test_interval_constants():
    """Test interval constants."""
    assert isinstance(DEFAULT_SCAN_INTERVAL, timedelta)
    assert DEFAULT_SCAN_INTERVAL.total_seconds() == 60  # 60 seconds
    
    assert isinstance(BACKOFF_INTERVAL_SECONDS, int)
    assert BACKOFF_INTERVAL_SECONDS == 90  # 90 seconds


def test_service_constants():
    """Test service-related constants."""
    assert SERVICE_START == "start"
    assert isinstance(SERVICE_START, str)


def test_config_field_constants():
    """Test configuration field constants."""
    assert CONF_SLUG == "slug"
    assert CONF_TIMEOUT_S == "timeout_s"
    assert CONF_DEVICE == "device"
    
    # All should be strings
    assert isinstance(CONF_SLUG, str)
    assert isinstance(CONF_TIMEOUT_S, str)
    assert isinstance(CONF_DEVICE, str)


def test_constant_types():
    """Test that constants have the expected types."""
    assert isinstance(DEFAULT_TIMEOUT_SECONDS, int)
    assert isinstance(MIN_TIMEOUT_SECONDS, int)
    assert isinstance(MAX_TIMEOUT_SECONDS, int)
    assert isinstance(BACKOFF_INTERVAL_SECONDS, int)
    assert isinstance(DEFAULT_SCAN_INTERVAL, timedelta)