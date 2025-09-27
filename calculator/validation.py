"""
Input validation utilities for the calculator application.
"""

import re
from typing import Tuple, Union

from .exceptions import InvalidInputError

Number = Union[int, float]


class InputValidator:
    """Validates and parses user input for the calculator."""

    @staticmethod
    def validate_number(input_str: str) -> Number:
        """
        Validate and convert string input to a number.

        Args:
            input_str: String input from user

        Returns:
            The converted number (int or float)

        Raises:
            InvalidInputError: If the input cannot be converted to a number
        """
        input_str = input_str.strip()

        if not input_str:
            raise InvalidInputError("Empty input is not a valid number")



        # Check for valid number pattern (including negative numbers and scientific notation)
        number_pattern = r"^[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?$"
        if not re.match(number_pattern, input_str):
            raise InvalidInputError(f"'{input_str}' is not a valid number format")

        try:
            # Try to convert to int first if it's a whole number
            if "." not in input_str and "e" not in input_str.lower():
                result = int(input_str)
            else:
                result = float(input_str)

            # Check for infinity or NaN
            if isinstance(result, float):
                if not (float("-inf") < result < float("inf")):
                    raise InvalidInputError(f"Number '{input_str}' is out of range")
                if result != result:  # Check for NaN  # pragma: no cover
                    raise InvalidInputError(f"'{input_str}' resulted in an invalid number")  # pragma: no cover

            return result

        except (ValueError, OverflowError):
            raise InvalidInputError(f"'{input_str}' is not a valid number")

    @staticmethod
    def validate_operation(operation_str: str) -> str:
        """
        Validate operation symbol.

        Args:
            operation_str: Operation symbol string

        Returns:
            Cleaned operation symbol

        Raises:
            InvalidInputError: If operation is invalid
        """
        operation_str = operation_str.strip()

        if not operation_str:
            raise InvalidInputError("Empty operation is not valid")

        valid_operations = {"+", "-", "*", "/"}
        if operation_str not in valid_operations:
            valid_ops = ", ".join(sorted(valid_operations))
            raise InvalidInputError(
                f"'{operation_str}' is not a valid operation. Valid operations: {valid_ops}"
            )

        return operation_str

    @staticmethod
    def parse_calculation_input(input_str: str) -> Tuple[Number, str, Number]:
        """
        Parse a calculation input string into components.

        Supports formats like:
        - "5 + 3"
        - "5+3"
        - "-5 * 2.5"
        - "10 / -3"

        Args:
            input_str: Complete calculation string

        Returns:
            Tuple of (first_number, operation, second_number)

        Raises:
            InvalidInputError: If input format is invalid
        """
        input_str = input_str.strip()

        if not input_str:
            raise InvalidInputError("Empty input")

        # Pattern to match calculation: number operator number
        # This handles negative numbers correctly
        pattern = r'^([-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?)\s*([\+\-\*/])\s*([-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?)$'
        
        match = re.match(pattern, input_str)
        if not match:
            raise InvalidInputError(
                "Invalid input format. Use: 'number operation number' (e.g., '5 + 3')"
            )

        first_str, operation_str, second_str = match.groups()

        # Validate and convert each component
        first_number = InputValidator.validate_number(first_str)
        operation = InputValidator.validate_operation(operation_str)
        second_number = InputValidator.validate_number(second_str)

        return first_number, operation, second_number