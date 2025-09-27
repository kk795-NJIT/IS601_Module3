# Python Calculator

[![Python Calculator CI/CD](https://github.com/yourusername/python-calculator/actions/workflows/ci.yml/badge.svg)](https://github.com/yourusername/python-calculator/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/yourusername/python-calculator/branch/main/graph/badge.svg)](https://codecov.io/gh/yourusername/python-calculator)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A robust command-line calculator implemented in Python using best practices, comprehensive testing, and continuous integration.

## Features

- **REPL Interface**: Interactive Read-Eval-Print Loop for seamless user experience
- **Arithmetic Operations**: Addition (+), Subtraction (-), Multiplication (*), Division (/)
- **Input Validation**: Comprehensive validation with regex patterns and error handling
- **Error Handling**: Custom exception hierarchy for specific error types
- **Object-Oriented Design**: Clean architecture using abstract base classes and polymorphism
- **Comprehensive Testing**: 99% test coverage with pytest and parameterized tests
- **Code Quality**: Enforced with black, flake8, and isort
- **CI/CD Pipeline**: GitHub Actions with multi-version Python testing

## Installation

### Prerequisites

- Python 3.9 or higher
- pip (Python package installer)

### Clone the Repository

```bash
git clone https://github.com/yourusername/python-calculator.git
cd python-calculator
```

### Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Run the calculator:

```bash
python main.py
```

### Interactive Examples

```
==================================================
      PYTHON CALCULATOR - REPL MODE
==================================================
Welcome to the Python Calculator!
Available operations: +, -, *, /

Calculator> 5 + 3
Result: 8

Calculator> 10.5 - 2.3
Result: 8.2

Calculator> 7 * 4
Result: 28

Calculator> 15 / 3
Result: 5.0

Calculator> help
==================================================
             CALCULATOR HELP
==================================================
Supported Operations:
  +, -, *, /

Input Format: number operation number
Examples: 5 + 3, 10.5 - 2.3, 7 * 4, 15 / 3
Commands: help, quit, exit
==================================================

Calculator> quit
Thank you for using the Python Calculator!
```

### Supported Input Formats

- **Integers**: `5`, `-10`, `0`
- **Decimals**: `3.14`, `-2.5`, `0.0`
- **Scientific notation**: `1e3`, `5.5e-1`
- **Whitespace tolerant**: `  5 + 3  ` works the same as `5+3`

### Commands

- `help` - Display help information
- `quit` or `exit` - Exit the calculator
- `Ctrl+C` - Force exit

## Development

### Project Structure

```
python-calculator/
├── calculator/
│   ├── __init__.py          # Package initialization
│   ├── exceptions.py        # Custom exception hierarchy
│   ├── operations.py        # Arithmetic operation classes
│   ├── calculator.py        # Main calculator class
│   ├── validation.py        # Input validation logic
│   └── cli.py              # Command-line interface
├── tests/
│   ├── __init__.py
│   ├── test_exceptions.py   # Exception tests
│   ├── test_operations.py   # Operation tests
│   ├── test_calculator.py   # Calculator tests
│   ├── test_validation.py   # Validation tests
│   ├── test_cli.py         # CLI tests
│   └── test_main.py        # Main entry point tests
├── .github/workflows/
│   └── ci.yml              # GitHub Actions CI/CD pipeline
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── pyproject.toml         # Project configuration
├── .flake8               # Flake8 configuration
├── .gitignore           # Git ignore rules
└── README.md           # This file
```

### Running Tests

```bash
# Run all tests
python -m pytest

# Run tests with coverage
python -m pytest --cov=calculator

# Run tests with detailed coverage report
python -m pytest --cov=calculator --cov-report=html

# Run tests with coverage enforcement (95% minimum)
python -m pytest --cov=calculator --cov-fail-under=95
```

### Code Quality Checks

```bash
# Format code with black
black .

# Sort imports with isort
isort .

# Lint code with flake8
flake8 .

# Run all quality checks together
black . && isort . && flake8 .
```

### Adding New Operations

1. Create a new operation class in `calculator/operations.py`:

```python
class Power(Operation):
    """Power operation implementation."""
    
    def execute(self, a: Number, b: Number) -> Number:
        """Raise a to the power of b."""
        try:
            result = a ** b
            if abs(result) > 1e308:
                raise OverflowError(f"Power result causes overflow")
            return result
        except (OverflowError, ValueError) as e:
            raise OverflowError(f"Power overflow: {a} ** {b}") from e
    
    def get_symbol(self) -> str:
        """Return the power symbol."""
        return "**"
    
    def get_name(self) -> str:
        """Return the operation name."""
        return "power"
```

2. Register the operation in `Calculator._register_operations()`:

```python
def _register_operations(self):
    """Register all available operations."""
    operations = [Addition(), Subtraction(), Multiplication(), Division(), Power()]
    for operation in operations:
        self._operations[operation.get_symbol()] = operation
```

3. Update the validation regex in `InputValidator` to support the new symbol:

```python
operation_pattern = r"^[+\-*/\*\*]$"  # Added \*\* for power
```

4. Add comprehensive tests in `tests/test_operations.py`

## Architecture

### Design Patterns

- **Strategy Pattern**: Operations are implemented as interchangeable strategies
- **Factory Pattern**: Calculator factory creates and manages operations
- **Facade Pattern**: Calculator class provides a simplified interface
- **Command Pattern**: CLI processes user commands through a consistent interface

### Object-Oriented Principles

- **Abstraction**: `Operation` abstract base class defines the interface
- **Inheritance**: Concrete operations inherit from the base class
- **Polymorphism**: Operations can be used interchangeably
- **Encapsulation**: Each class has clear responsibilities and boundaries

### Error Handling

Custom exception hierarchy provides specific error types:

```python
CalculatorError                    # Base exception
├── InvalidInputError             # Invalid user input
├── InvalidOperationError         # Unsupported operation
├── DivisionByZeroError          # Division by zero
└── OverflowError                # Numeric overflow
```

## Testing

The project achieves **99% test coverage** with comprehensive test suites:

- **Unit Tests**: Test individual components in isolation
- **Integration Tests**: Test component interactions
- **Parameterized Tests**: Test multiple scenarios efficiently
- **Edge Case Testing**: Handle boundary conditions and error states
- **Mock Testing**: Isolate components for focused testing

### Test Categories

1. **Exception Tests**: Verify custom exception behavior
2. **Operation Tests**: Test arithmetic operations with various inputs
3. **Calculator Tests**: Test calculator logic and error handling
4. **Validation Tests**: Test input validation and parsing
5. **CLI Tests**: Test user interface and command processing
6. **Main Tests**: Test application entry point

## Continuous Integration

GitHub Actions pipeline includes:

- **Multi-version Testing**: Python 3.9, 3.10, 3.11, 3.12
- **Code Quality**: black, flake8, isort checks
- **Test Coverage**: Enforced 95% minimum coverage
- **Security Scanning**: bandit and safety checks
- **Integration Testing**: End-to-end functionality verification

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass and maintain 95%+ coverage
6. Run code quality checks
7. Commit your changes (`git commit -m 'Add amazing feature'`)
8. Push to the branch (`git push origin feature/amazing-feature`)
9. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Write comprehensive tests for new features
- Maintain or improve test coverage
- Add docstrings to all public methods
- Use type hints for better code documentation
- Follow the existing code structure and patterns

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Python community for excellent testing and development tools
- GitHub Actions for continuous integration platform
- Contributors and maintainers of pytest, black, flake8, and other development tools