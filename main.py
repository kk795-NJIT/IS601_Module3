"""
Main entry point for the command-line calculator application.
"""

from calculator.cli import CalculatorCLI


def main():
    """Main function to start the calculator application."""
    try:
        cli = CalculatorCLI()
        cli.run()
    except Exception as e:
        print(f"Failed to start calculator: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
