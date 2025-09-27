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
