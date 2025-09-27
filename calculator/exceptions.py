"""
Custom exceptions for the calculator application.
"""


class CalculatorError(Exception):
    """Base exception class for calculator errors."""

    pass


class InvalidInputError(CalculatorError):
    """Raised when user provides invalid input."""

    pass


class InvalidOperationError(CalculatorError):
    """Raised when an invalid operation is requested."""

    pass


class DivisionByZeroError(CalculatorError):
    """Raised when attempting to divide by zero."""

    pass


class OverflowError(CalculatorError):
    """Raised when a calculation results in overflow."""

    pass
