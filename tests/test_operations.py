"""Unit tests for arithmetic operations."""

import pytest

from calculator.exceptions import DivisionByZeroError, OverflowError
from calculator.operations import Addition, Division, Multiplication, Subtraction


class TestAddition:
    """Test class for Addition operation."""

    def setup_method(self):
        """Set up test fixtures."""
        self.operation = Addition()

    def test_execute_positive_numbers(self):
        """Test addition of positive numbers."""
        assert self.operation.execute(5, 3) == 8

    def test_execute_negative_numbers(self):
        """Test addition of negative numbers."""
        assert self.operation.execute(-5, -3) == -8

    def test_execute_mixed_numbers(self):
        """Test addition of mixed positive and negative numbers."""
        assert self.operation.execute(-5, 3) == -2

    def test_execute_zero(self):
        """Test addition with zero."""
        assert self.operation.execute(5, 0) == 5

    def test_get_symbol(self):
        """Test get_symbol method."""
        assert self.operation.get_symbol() == "+"

    def test_get_name(self):
        """Test get_name method."""
        assert self.operation.get_name() == "addition"

    def test_execute_overflow(self):
        """Test addition overflow handling."""
        large_num = 10**308
        with pytest.raises(OverflowError):
            self.operation.execute(large_num, large_num)


class TestSubtraction:
    """Test class for Subtraction operation."""

    def setup_method(self):
        """Set up test fixtures."""
        self.operation = Subtraction()

    def test_execute_positive_numbers(self):
        """Test subtraction of positive numbers."""
        assert self.operation.execute(10, 4) == 6

    def test_execute_negative_numbers(self):
        """Test subtraction of negative numbers."""
        assert self.operation.execute(-10, -4) == -6

    def test_execute_mixed_numbers(self):
        """Test subtraction of mixed positive and negative numbers."""
        assert self.operation.execute(-5, 3) == -8

    def test_get_symbol(self):
        """Test get_symbol method."""
        assert self.operation.get_symbol() == "-"

    def test_get_name(self):
        """Test get_name method."""
        assert self.operation.get_name() == "subtraction"

    def test_execute_overflow(self):
        """Test subtraction overflow handling."""
        large_num = 10**308
        with pytest.raises(OverflowError):
            self.operation.execute(-large_num, large_num)


class TestMultiplication:
    """Test class for Multiplication operation."""

    def setup_method(self):
        """Set up test fixtures."""
        self.operation = Multiplication()

    def test_execute_positive_numbers(self):
        """Test multiplication of positive numbers."""
        assert self.operation.execute(3, 7) == 21

    def test_execute_negative_numbers(self):
        """Test multiplication of negative numbers."""
        assert self.operation.execute(-3, -7) == 21

    def test_execute_mixed_numbers(self):
        """Test multiplication of mixed positive and negative numbers."""
        assert self.operation.execute(-3, 7) == -21

    def test_execute_zero(self):
        """Test multiplication with zero."""
        assert self.operation.execute(5, 0) == 0

    def test_get_symbol(self):
        """Test get_symbol method."""
        assert self.operation.get_symbol() == "*"

    def test_get_name(self):
        """Test get_name method."""
        assert self.operation.get_name() == "multiplication"

    def test_execute_overflow(self):
        """Test multiplication overflow handling."""
        large_num = 10**200
        with pytest.raises(OverflowError):
            self.operation.execute(large_num, large_num)


class TestDivision:
    """Test class for Division operation."""

    def setup_method(self):
        """Set up test fixtures."""
        self.operation = Division()

    def test_execute_positive_numbers(self):
        """Test division of positive numbers."""
        assert self.operation.execute(15, 3) == 5.0

    def test_execute_negative_numbers(self):
        """Test division of negative numbers."""
        assert self.operation.execute(-15, -3) == 5.0

    def test_execute_mixed_numbers(self):
        """Test division of mixed positive and negative numbers."""
        assert self.operation.execute(-15, 3) == -5.0

    def test_execute_division_by_zero(self):
        """Test division by zero raises exception."""
        with pytest.raises(DivisionByZeroError):
            self.operation.execute(5, 0)

    def test_get_symbol(self):
        """Test get_symbol method."""
        assert self.operation.get_symbol() == "/"

    def test_get_name(self):
        """Test get_name method."""
        assert self.operation.get_name() == "division"

    def test_execute_overflow(self):
        """Test division overflow handling."""
        large_num = 10**308
        small_num = 10**-308
        with pytest.raises(OverflowError):
            self.operation.execute(large_num, small_num)


# Parameterized tests as required by assignment
class TestOperationsParameterized:
    """Parameterized tests for all operations covering various input scenarios."""

    @pytest.mark.parametrize(
        "operation_name, symbol, name",
        [
            ("Addition", "+", "addition"),
            ("Subtraction", "-", "subtraction"),
            ("Multiplication", "*", "multiplication"),
            ("Division", "/", "division"),
        ],
    )
    def test_operation_properties(self, operation_name, symbol, name):
        """Test that operations have correct symbols and names."""
        operation_classes = {
            "Addition": Addition,
            "Subtraction": Subtraction,
            "Multiplication": Multiplication,
            "Division": Division,
        }
        operation = operation_classes[operation_name]()
        assert operation.get_symbol() == symbol
        assert operation.get_name() == name

    @pytest.mark.parametrize(
        "operation_name, a, b, expected",
        [
            # Addition test cases
            ("Addition", 5, 3, 8),
            ("Addition", -2, 4, 2),
            ("Addition", 0, 0, 0),
            ("Addition", -5, -3, -8),
            ("Addition", 2.5, 1.5, 4.0),
            # Subtraction test cases
            ("Subtraction", 10, 3, 7),
            ("Subtraction", -2, -4, 2),
            ("Subtraction", 5, 5, 0),
            ("Subtraction", 0, 3, -3),
            ("Subtraction", 5.5, 2.0, 3.5),
            # Multiplication test cases
            ("Multiplication", 3, 4, 12),
            ("Multiplication", -2, 3, -6),
            ("Multiplication", 0, 5, 0),
            ("Multiplication", -3, -4, 12),
            ("Multiplication", 2.0, 3.5, 7.0),
            # Division test cases
            ("Division", 10, 2, 5.0),
            ("Division", -6, 3, -2.0),
            ("Division", 7, 2, 3.5),
            ("Division", -12, -3, 4.0),
            ("Division", 7.5, 2.5, 3.0),
        ],
    )
    def test_operation_calculations(self, operation_name, a, b, expected):
        """Test operations with various input combinations."""
        operation_classes = {
            "Addition": Addition,
            "Subtraction": Subtraction,
            "Multiplication": Multiplication,
            "Division": Division,
        }
        operation = operation_classes[operation_name]()
        result = operation.execute(a, b)
        if isinstance(expected, float):
            assert pytest.approx(result) == expected
        else:
            assert result == expected

    @pytest.mark.parametrize(
        "operation_name",
        ["Addition", "Subtraction", "Multiplication", "Division"],
    )
    def test_operation_overflow_handling(self, operation_name):
        """Test that all operations handle overflow correctly."""
        operation_classes = {
            "Addition": Addition,
            "Subtraction": Subtraction,
            "Multiplication": Multiplication,
            "Division": Division,
        }
        operation = operation_classes[operation_name]()
        large_num = 10**308

        with pytest.raises(OverflowError):
            if operation_name == "Division":
                # For division, use small denominator to cause overflow
                operation.execute(large_num, 10**-308)
            elif operation_name == "Subtraction":
                # For subtraction, subtract a large negative from a large positive
                operation.execute(large_num, -large_num)
            else:
                # For addition and multiplication, use large numbers
                operation.execute(large_num, large_num)

    @pytest.mark.parametrize(
        "zero_value",
        [0, 0.0, -0.0],
    )
    def test_division_by_zero_variations(self, zero_value):
        """Test division by zero with different zero representations."""
        operation = Division()
        with pytest.raises(
            DivisionByZeroError, match="Division by zero is not allowed"
        ):
            operation.execute(10, zero_value)
