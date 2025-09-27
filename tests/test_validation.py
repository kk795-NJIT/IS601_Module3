"""Unit tests for input validation functionality."""

import pytest
from unittest.mock import patch
from calculator.exceptions import InvalidInputError
from calculator.validation import InputValidator


class TestInputValidator:
    """Test class for InputValidator functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        self.validator = InputValidator()

    def test_validate_number_valid_integers(self):
        """Test validation of valid integers."""
        assert self.validator.validate_number("5") == 5
        assert self.validator.validate_number("-5") == -5
        assert self.validator.validate_number("0") == 0

    def test_validate_number_valid_floats(self):
        """Test validation of valid floats."""
        assert self.validator.validate_number("5.0") == 5.0
        assert self.validator.validate_number("3.14") == 3.14
        assert self.validator.validate_number("-2.5") == -2.5

    def test_validate_number_scientific_notation(self):
        """Test validation of scientific notation."""
        assert self.validator.validate_number("1e3") == 1000.0
        assert self.validator.validate_number("5.5e-1") == 0.55

    def test_validate_number_with_whitespace(self):
        """Test validation with whitespace."""
        assert self.validator.validate_number("  5  ") == 5

    def test_validate_number_invalid_strings(self):
        """Test validation of invalid strings."""
        with pytest.raises(InvalidInputError):
            self.validator.validate_number("")
        with pytest.raises(InvalidInputError):
            self.validator.validate_number("  ")
        with pytest.raises(InvalidInputError):
            self.validator.validate_number("abc")
        with pytest.raises(InvalidInputError):
            self.validator.validate_number("5a")

    def test_validate_number_special_values(self):
        """Test validation of special values."""
        with pytest.raises(InvalidInputError):
            self.validator.validate_number("inf")
        with pytest.raises(InvalidInputError):
            self.validator.validate_number("nan")

    def test_validate_number_overflow(self):
        """Test overflow handling."""
        with patch('builtins.int', side_effect=OverflowError("overflow")):
            with pytest.raises(InvalidInputError):
                self.validator.validate_number("999")

    def test_validate_number_out_of_range(self):
        """Test out of range handling."""
        with pytest.raises(InvalidInputError, match="is out of range"):
            self.validator.validate_number("1e400")

    def test_validate_operation_valid(self):
        """Test validation of valid operations."""
        assert self.validator.validate_operation("+") == "+"
        assert self.validator.validate_operation("-") == "-"
        assert self.validator.validate_operation("*") == "*"
        assert self.validator.validate_operation("/") == "/"
        assert self.validator.validate_operation("  +  ") == "+"

    def test_validate_operation_invalid(self):
        """Test validation of invalid operations."""
        with pytest.raises(InvalidInputError):
            self.validator.validate_operation("")
        with pytest.raises(InvalidInputError):
            self.validator.validate_operation("  ")
        with pytest.raises(InvalidInputError):
            self.validator.validate_operation("@")
        with pytest.raises(InvalidInputError):
            self.validator.validate_operation("add")

    def test_parse_calculation_input_valid(self):
        """Test parsing of valid calculation inputs."""
        first, op, second = self.validator.parse_calculation_input("5 + 3")
        assert first == 5
        assert op == "+"
        assert second == 3

        first, op, second = self.validator.parse_calculation_input("10-2")
        assert first == 10
        assert op == "-"
        assert second == 2

        first, op, second = self.validator.parse_calculation_input("3.14 * 2.86")
        assert pytest.approx(first, rel=1e-9) == 3.14
        assert op == "*"
        assert pytest.approx(second, rel=1e-9) == 2.86

    def test_parse_calculation_input_invalid(self):
        """Test parsing of invalid calculation inputs."""
        with pytest.raises(InvalidInputError):
            self.validator.parse_calculation_input("")
        with pytest.raises(InvalidInputError):
            self.validator.parse_calculation_input("5")
        with pytest.raises(InvalidInputError):
            self.validator.parse_calculation_input("5 +")
        with pytest.raises(InvalidInputError):
            self.validator.parse_calculation_input("+ 3")
        with pytest.raises(InvalidInputError):
            self.validator.parse_calculation_input("abc + 3")


