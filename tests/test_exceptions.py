"""Test Wolt Watch exceptions."""
from __future__ import annotations

import sys
from pathlib import Path
import pytest

# Add the custom_components directory to sys.path for importing
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir / "custom_components"))

# Import the exceptions directly from the file
import importlib.util
spec = importlib.util.spec_from_file_location(
    "exceptions", 
    root_dir / "custom_components" / "wolt_watch" / "exceptions.py"
)
exceptions_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(exceptions_module)

# Extract exception classes
WoltWatchException = exceptions_module.WoltWatchException
WoltWatchConnectionError = exceptions_module.WoltWatchConnectionError
WoltWatchConfigurationError = exceptions_module.WoltWatchConfigurationError
WoltWatchAPIError = exceptions_module.WoltWatchAPIError


def test_base_exception():
    """Test base WoltWatchException."""
    exception = WoltWatchException("Test error")
    assert str(exception) == "Test error"
    assert isinstance(exception, Exception)


def test_connection_error():
    """Test WoltWatchConnectionError."""
    exception = WoltWatchConnectionError("Connection failed")
    assert str(exception) == "Connection failed"
    assert isinstance(exception, WoltWatchException)
    assert isinstance(exception, Exception)


def test_configuration_error():
    """Test WoltWatchConfigurationError."""
    exception = WoltWatchConfigurationError("Invalid config")
    assert str(exception) == "Invalid config"
    assert isinstance(exception, WoltWatchException)
    assert isinstance(exception, Exception)


def test_api_error():
    """Test WoltWatchAPIError."""
    exception = WoltWatchAPIError("API failed")
    assert str(exception) == "API failed"
    assert isinstance(exception, WoltWatchException)
    assert isinstance(exception, Exception)


def test_exception_hierarchy():
    """Test that all custom exceptions inherit properly."""
    # All custom exceptions should inherit from WoltWatchException
    assert issubclass(WoltWatchConnectionError, WoltWatchException)
    assert issubclass(WoltWatchConfigurationError, WoltWatchException)
    assert issubclass(WoltWatchAPIError, WoltWatchException)
    
    # And ultimately from Exception
    assert issubclass(WoltWatchException, Exception)
    assert issubclass(WoltWatchConnectionError, Exception)
    assert issubclass(WoltWatchConfigurationError, Exception)
    assert issubclass(WoltWatchAPIError, Exception)