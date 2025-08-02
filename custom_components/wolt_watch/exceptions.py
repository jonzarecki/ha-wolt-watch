"""Exceptions for Wolt Watch integration."""
from __future__ import annotations


class WoltWatchException(Exception):
    """Base exception for Wolt Watch."""


class WoltWatchConnectionError(WoltWatchException):
    """Exception for connection errors."""


class WoltWatchConfigurationError(WoltWatchException):
    """Exception for configuration errors."""


class WoltWatchAPIError(WoltWatchException):
    """Exception for API errors."""