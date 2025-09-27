"""
Unit tests for custom exceptions.
"""

from calculator.exceptions import (
    CalculatorError,
    DivisionByZeroError,
    InvalidInputError,
    InvalidOperationError,
    OverflowError,
)


class TestCalculatorExceptions:
    """Test class for calculator exceptions."""

    def test_calculator_error_inheritance(self):
        """Test that all custom exceptions inherit from CalculatorError."""
        assert issubclass(InvalidInputError, CalculatorError)
        assert issubclass(InvalidOperationError, CalculatorError)
        assert issubclass(DivisionByZeroError, CalculatorError)
        assert issubclass(OverflowError, CalculatorError)

    def test_calculator_error_creation(self):
        """Test creating CalculatorError with message."""
        error = CalculatorError("Test error")
        assert str(error) == "Test error"

    def test_invalid_input_error_creation(self):
        """Test creating InvalidInputError with message."""
        error = InvalidInputError("Invalid input")
        assert str(error) == "Invalid input"

    def test_invalid_operation_error_creation(self):
        """Test creating InvalidOperationError with message."""
        error = InvalidOperationError("Invalid operation")
        assert str(error) == "Invalid operation"

    def test_division_by_zero_error_creation(self):
        """Test creating DivisionByZeroError with message."""
        error = DivisionByZeroError("Division by zero")
        assert str(error) == "Division by zero"

    def test_overflow_error_creation(self):
        """Test creating OverflowError with message."""
        error = OverflowError("Overflow occurred")
        assert str(error) == "Overflow occurred"

    def test_exceptions_are_exceptions(self):
        """Test that all custom exceptions are proper Exception instances."""
        errors = [
            CalculatorError("test"),
            InvalidInputError("test"),
            InvalidOperationError("test"),
            DivisionByZeroError("test"),
            OverflowError("test"),
        ]

        for error in errors:
            assert isinstance(error, Exception)
            assert isinstance(error, CalculatorError)
