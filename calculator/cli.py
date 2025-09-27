"""Command-line interface for the calculator with REPL functionality."""

import sys
from typing import Optional

from .calculator import Calculator
from .exceptions import (
    CalculatorError,
    DivisionByZeroError,
    InvalidInputError,
    InvalidOperationError,
    OverflowError,
)
from .validation import InputValidator


class CalculatorCLI:
    """Command-line interface for the calculator using REPL pattern."""

    def __init__(self):
        """Initialize the CLI with calculator and validator instances."""
        self.calculator = Calculator()
        self.validator = InputValidator()

    def display_welcome(self) -> None:
        """Display welcome message and instructions."""
        print("=" * 50)
        print("      PYTHON CALCULATOR - REPL MODE")
        print("=" * 50)
        print("Welcome to the Python Calculator!")
        print(
            "Available operations:",
            ", ".join(self.calculator.get_available_operations()),
        )
        print("Instructions:")
        print("• Enter calculations like: 5 + 3, 10 - 2, 7 * 4, 15 / 3")
        print("• Type 'help' for more information")
        print("• Type 'quit' or 'exit' to close the calculator")
        print("• Press Ctrl+C to exit at any time")
        print("-" * 50)

    def display_help(self) -> None:
        """Display detailed help information."""
        print("=" * 50)
        print("             CALCULATOR HELP")
        print("=" * 50)
        print("Supported Operations:")
        for operation in self.calculator.get_available_operations():
            print(f"  {operation}")
        print("Input Format: number operation number")
        print("Examples: 5 + 3, 10.5 - 2.3, 7 * 4, 15 / 3")
        print("Commands: help, quit, exit")
        print("=" * 50)

    def _handle_calculation(self, user_input: str) -> bool:
        """Handle calculation input and return True to continue."""
        try:
            first_num, operation, second_num = self.validator.parse_calculation_input(
                user_input
            )
            result = self.calculator.calculate(first_num, operation, second_num)
            print(f"Result: {result}")
            return True
        except InvalidInputError as e:
            print(f"Input Error: {e}")
            return True
        except InvalidOperationError as e:
            print(f"Operation Error: {e}")
            return True
        except DivisionByZeroError as e:
            print(f"Math Error: {e}")
            return True
        except OverflowError as e:
            print(f"Overflow Error: {e}")
            return True
        except CalculatorError as e:
            print(f"Calculator Error: {e}")
            return True
        except Exception as e:
            print(f"Unexpected error: {e}")
            return True

    def process_input(self, user_input: str) -> Optional[bool]:
        """Process user input and perform calculation or command."""
        cleaned_input = user_input.strip().lower()

        if cleaned_input in ("quit", "exit"):
            return False

        if cleaned_input == "help":
            self.display_help()
            return True

        if not cleaned_input:
            return True

        return self._handle_calculation(user_input)

    def run(self) -> None:
        """Run the REPL (Read-Eval-Print Loop)."""
        self.display_welcome()

        try:
            while True:
                try:
                    user_input = input("Calculator> ").strip()

                    result = self.process_input(user_input)

                    if result is False:
                        print("Thank you for using the Python Calculator!")
                        break

                except EOFError:
                    print("Goodbye!")
                    break

        except KeyboardInterrupt:
            print("Calculator interrupted by user. Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"Unexpected error in main loop: {e}")
            sys.exit(1)
