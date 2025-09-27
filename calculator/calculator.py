"""
Main Calculator class that manages operations and performs calculations.
"""

from typing import Dict, Type, Union

from .exceptions import InvalidOperationError
from .operations import Addition, Division, Multiplication, Number, Operation, Subtraction


class Calculator:
    """Main calculator class implementing the facade pattern."""

    def __init__(self):
        """Initialize calculator with available operations."""
        self._operations: Dict[str, Operation] = {}
        self._register_operations()

    def _register_operations(self) -> None:
        """Register all available operations with their symbols."""
        operations = [Addition(), Subtraction(), Multiplication(), Division()]
        
        for operation in operations:
            self._operations[operation.get_symbol()] = operation

    def calculate(self, first_number: Number, operation_symbol: str, second_number: Number) -> Number:
        """
        Perform calculation with given numbers and operation.

        Args:
            first_number: First operand
            operation_symbol: Symbol representing the operation (+, -, *, /)
            second_number: Second operand

        Returns:
            Result of the calculation

        Raises:
            InvalidOperationError: If operation symbol is not supported
            DivisionByZeroError: If attempting to divide by zero
            OverflowError: If calculation results in overflow
        """
        if not self.is_valid_operation(operation_symbol):
            valid_ops = ", ".join(self._operations.keys())
            raise InvalidOperationError(
                f"Invalid operation '{operation_symbol}'. Valid operations: {valid_ops}"
            )

        operation = self._operations[operation_symbol]
        return operation.execute(first_number, second_number)

    def is_valid_operation(self, operation_symbol: str) -> bool:
        """
        Check if an operation symbol is valid.

        Args:
            operation_symbol: Symbol to validate

        Returns:
            True if valid, False otherwise
        """
        return operation_symbol in self._operations

    def get_available_operations(self) -> Dict[str, str]:
        """
        Get all available operations with their symbols and names.

        Returns:
            Dictionary mapping symbols to operation names
        """
        return {symbol: op.get_name() for symbol, op in self._operations.items()}