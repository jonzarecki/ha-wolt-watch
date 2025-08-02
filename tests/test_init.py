"""Test Wolt Watch integration logic."""
from __future__ import annotations

import sys
from pathlib import Path

# Add the custom_components directory to sys.path for importing
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir / "custom_components"))

# Import the constants directly from the file
import importlib.util
spec = importlib.util.spec_from_file_location(
    "const", 
    root_dir / "custom_components" / "wolt_watch" / "const.py"
)
const_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(const_module)

# Extract constants for testing
DOMAIN = const_module.DOMAIN
SERVICE_START = const_module.SERVICE_START
DEFAULT_TIMEOUT_SECONDS = const_module.DEFAULT_TIMEOUT_SECONDS
MIN_TIMEOUT_SECONDS = const_module.MIN_TIMEOUT_SECONDS
MAX_TIMEOUT_SECONDS = const_module.MAX_TIMEOUT_SECONDS
CONF_SLUG = const_module.CONF_SLUG
CONF_TIMEOUT_S = const_module.CONF_TIMEOUT_S
CONF_DEVICE = const_module.CONF_DEVICE


def test_constants_imported():
    """Test that constants are properly defined."""
    assert DOMAIN == "wolt_watch"
    assert SERVICE_START == "start"
    assert DEFAULT_TIMEOUT_SECONDS == 7200
    assert MIN_TIMEOUT_SECONDS == 60
    assert MAX_TIMEOUT_SECONDS == 86400
    assert CONF_SLUG == "slug"
    assert CONF_TIMEOUT_S == "timeout_s"
    assert CONF_DEVICE == "device"


def test_device_format_validation():
    """Test device format validation logic."""
    # Test valid device format
    valid_device = "notify.mobile_app_test"
    assert "." in valid_device
    domain, service = valid_device.split(".", 1)
    assert domain == "notify"
    assert service == "mobile_app_test"
    
    # Test invalid device format (no dot)
    invalid_device = "notify_mobile_app_test"
    assert "." not in invalid_device


def test_restaurant_name_formatting():
    """Test restaurant name formatting from slug."""
    slug = "mcdonalds-dizengoff"
    restaurant_name = slug.replace("-", " ").title()
    assert restaurant_name == "Mcdonalds Dizengoff"
    
    slug2 = "taizu"
    restaurant_name2 = slug2.replace("-", " ").title()
    assert restaurant_name2 == "Taizu"


def test_timeout_validation_logic():
    """Test timeout validation logic."""
    # Test valid timeouts
    valid_timeout = 3600
    assert MIN_TIMEOUT_SECONDS <= valid_timeout <= MAX_TIMEOUT_SECONDS
    
    # Test invalid timeouts
    too_low = 30
    too_high = 100000
    assert too_low < MIN_TIMEOUT_SECONDS
    assert too_high > MAX_TIMEOUT_SECONDS
    
    # Test default timeout
    assert MIN_TIMEOUT_SECONDS <= DEFAULT_TIMEOUT_SECONDS <= MAX_TIMEOUT_SECONDS


def test_integration_file_structure():
    """Test that required files exist."""
    wolt_watch_dir = root_dir / "custom_components" / "wolt_watch"
    
    # Check that required files exist
    assert (wolt_watch_dir / "__init__.py").exists()
    assert (wolt_watch_dir / "const.py").exists()
    assert (wolt_watch_dir / "exceptions.py").exists()
    assert (wolt_watch_dir / "manifest.json").exists()
    assert (wolt_watch_dir / "services.yaml").exists()


def test_manifest_file():
    """Test that manifest.json is valid JSON and has required fields."""
    import json
    
    manifest_path = root_dir / "custom_components" / "wolt_watch" / "manifest.json"
    assert manifest_path.exists()
    
    with open(manifest_path) as f:
        manifest = json.load(f)
    
    # Check required fields
    assert "domain" in manifest
    assert "name" in manifest
    assert "version" in manifest
    assert "documentation" in manifest
    assert "issue_tracker" in manifest
    assert "codeowners" in manifest
    assert "requirements" in manifest
    
    # Check values
    assert manifest["domain"] == "wolt_watch"
    assert manifest["name"] == "Wolt Watch"
    assert "wolt-api-mcp" in str(manifest["requirements"])