"""Common fixtures for Wolt Watch tests."""
from __future__ import annotations

import pytest
from unittest.mock import Mock


@pytest.fixture
def mock_wolt_api():
    """Mock WoltAPI instance."""
    mock_api = Mock()
    mock_api.is_restaurant_open.return_value = False
    return mock_api


@pytest.fixture
def mock_hass():
    """Mock Home Assistant instance."""
    hass = Mock()
    hass.services = Mock()
    hass.services.async_call = Mock()
    hass.services.async_register = Mock()
    hass.services.has_service = Mock(return_value=True)
    hass.async_create_task = Mock()
    hass.async_add_executor_job = Mock()
    return hass