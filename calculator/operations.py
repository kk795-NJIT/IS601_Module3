"""
Operation classes implementing arithmetic operations using OOP principles.
"""

from abc import ABC, abstractmethod
from typing import Union

from .exceptions import DivisionByZeroError, OverflowError

Number = Union[int, float]


class Operation(ABC):
    """Abstract base class for all mathematical operations."""

    @abstractmethod
    def execute(self, a: Number, b: Number) -> Number:
        """
        Execute the operation on two numbers.

        Args:
            a: First operand
            b: Second operand

        Returns:
            Result of the operation

        Raises:
            CalculatorError: If operation cannot be performed
        """
        pass

    @abstractmethod
    def get_symbol(self) -> str:
        """Get the symbol representing this operation."""
        pass

    @abstractmethod
    def get_name(self) -> str:
        """Get the human-readable name of this operation."""
        pass


class Addition(Operation):
    """Addition operation implementation."""

    def execute(self, a: Number, b: Number) -> Number:
        """Add two numbers."""
        try:
            result = a + b
            # Check for overflow in extreme cases
            if abs(result) > 1e308:
                raise OverflowError(f"Addition result {result} causes overflow")
            return result
        except (OverflowError, ValueError) as e:
            raise OverflowError(f"Addition overflow: {a} + {b}") from e

    def get_symbol(self) -> str:
        """Return the addition symbol."""
        return "+"

    def get_name(self) -> str:
        """Return the operation name."""
        return "addition"


class Subtraction(Operation):
    """Subtraction operation implementation."""

    def execute(self, a: Number, b: Number) -> Number:
        """Subtract second number from first."""
        try:
            result = a - b
            # Check for overflow in extreme cases
            if abs(result) > 1e308:
                raise OverflowError(f"Subtraction result {result} causes overflow")
            return result
        except (OverflowError, ValueError) as e:
            raise OverflowError(f"Subtraction overflow: {a} - {b}") from e

    def get_symbol(self) -> str:
        """Return the subtraction symbol."""
        return "-"

    def get_name(self) -> str:
        """Return the operation name."""
        return "subtraction"


class Multiplication(Operation):
    """Multiplication operation implementation."""

    def execute(self, a: Number, b: Number) -> Number:
        """Multiply two numbers."""
        try:
            result = a * b
            # Check for overflow in extreme cases
            if abs(result) > 1e308:
                raise OverflowError(f"Multiplication result {result} causes overflow")
            return result
        except (OverflowError, ValueError) as e:
            raise OverflowError(f"Multiplication overflow: {a} * {b}") from e

    def get_symbol(self) -> str:
        """Return the multiplication symbol."""
        return "*"

    def get_name(self) -> str:
        """Return the operation name."""
        return "multiplication"


class Division(Operation):
    """Division operation implementation."""

    def execute(self, a: Number, b: Number) -> Number:
        """Divide first number by second."""
        if b == 0:
            raise DivisionByZeroError("Division by zero is not allowed")

        try:
            result = a / b
            # Check for overflow in extreme cases
            if abs(result) > 1e308:
                raise OverflowError(f"Division result {result} causes overflow")
            return result
        except (OverflowError, ValueError) as e:
            raise OverflowError(f"Division overflow: {a} / {b}") from e

    def get_symbol(self) -> str:
        """Return the division symbol."""
        return "/"

    def get_name(self) -> str:
        """Return the operation name."""
        return "division"
