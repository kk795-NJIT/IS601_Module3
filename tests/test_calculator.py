"""
Unit tests for the main Calculator class.
"""

import pytest

from calculator.calculator import Calculator
from calculator.exceptions import (
    DivisionByZeroError,
    InvalidOperationError,
    OverflowError,
)


class TestCalculator:
    """Test class for Calculator functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        self.calculator = Calculator()

    def test_calculator_initialization(self):
        """Test calculator is properly initialized."""
        assert self.calculator is not None
        assert hasattr(self.calculator, "_operations")
        assert len(self.calculator._operations) == 4

    def test_get_available_operations(self):
        """Test getting available operations."""
        operations = self.calculator.get_available_operations()
        expected_operations = {
            "+": "addition",
            "-": "subtraction",
            "*": "multiplication",
            "/": "division",
        }
        assert operations == expected_operations

    @pytest.mark.parametrize(
        "first, operation, second, expected",
        [
            (5, "+", 3, 8),
            (10, "-", 4, 6),
            (3, "*", 7, 21),
            (15, "/", 3, 5.0),
            (0, "+", 0, 0),
            (-5, "+", 5, 0),
            (-10, "-", -5, -5),
            (-3, "*", -4, 12),
            (-12, "/", -3, 4.0),
            (2.5, "+", 1.5, 4.0),
            (5.5, "-", 2.0, 3.5),
            (2.0, "*", 3.5, 7.0),
            (7.5, "/", 2.5, 3.0),
        ],
    )
    def test_calculate_valid_operations(self, first, operation, second, expected):
        """Test calculation with valid inputs."""
        result = self.calculator.calculate(first, operation, second)
        if isinstance(expected, float):
            assert pytest.approx(result) == expected
        else:
            assert result == expected

    @pytest.mark.parametrize(
        "operation",
        ["@", "#", "%", "^", "&", "add", "subtract", "multiply", "divide", ""],
    )
    def test_calculate_invalid_operation(self, operation):
        """Test calculation with invalid operations."""
        with pytest.raises(InvalidOperationError):
            self.calculator.calculate(5, operation, 3)

    def test_calculate_division_by_zero(self):
        """Test division by zero handling."""
        with pytest.raises(
            DivisionByZeroError, match="Division by zero is not allowed"
        ):
            self.calculator.calculate(10, "/", 0)

    @pytest.mark.parametrize(
        "operation",
        ["+", "-", "*", "/"],
    )
    def test_is_valid_operation_valid(self, operation):
        """Test validation of valid operations."""
        assert self.calculator.is_valid_operation(operation) is True

    @pytest.mark.parametrize(
        "operation",
        [
            "@",
            "#",
            "%",
            "^",
            "&",
            "add",
            "subtract",
            "multiply",
            "divide",
            "",
            "++",
            "--",
        ],
    )
    def test_is_valid_operation_invalid(self, operation):
        """Test validation of invalid operations."""
        assert self.calculator.is_valid_operation(operation) is False

    def test_calculate_overflow_handling(self):
        """Test overflow handling in calculations."""
        large_number = 1e200

        with pytest.raises(OverflowError):
            self.calculator.calculate(large_number, "*", large_number)

    def test_calculator_state_independence(self):
        """Test that calculator operations don't affect internal state."""
        result1 = self.calculator.calculate(5, "+", 3)
        result2 = self.calculator.calculate(10, "*", 2)
        result3 = self.calculator.calculate(15, "/", 3)

        assert result1 == 8
        assert result2 == 20
        assert result3 == 5.0

        operations = self.calculator.get_available_operations()
        assert len(operations) == 4

    def test_error_messages_contain_valid_operations(self):
        """Test that error messages include valid operations."""
        try:
            self.calculator.calculate(5, "@", 3)
        except InvalidOperationError as e:
            error_message = str(e)
            assert "Invalid operation '@'" in error_message
            assert "Valid operations:" in error_message
            assert "+" in error_message
            assert "-" in error_message
            assert "*" in error_message
            assert "/" in error_message
