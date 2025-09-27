"""Unit tests for the CLI interface."""

import pytest
from unittest.mock import patch, MagicMock
from calculator.cli import CalculatorCLI


class TestCalculatorCLI:
    """Test class for CalculatorCLI functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        self.cli = CalculatorCLI()

    def test_cli_initialization(self):
        """Test CLI initialization."""
        assert self.cli.calculator is not None
        assert self.cli.validator is not None

    @patch('builtins.print')
    def test_display_welcome(self, mock_print):
        """Test welcome message display."""
        self.cli.display_welcome()
        mock_print.assert_called()

    @patch('builtins.print')
    def test_display_help(self, mock_print):
        """Test help message display."""
        self.cli.display_help()
        mock_print.assert_called()

    def test_process_input_quit(self):
        """Test quit command."""
        assert self.cli.process_input("quit") is False
        assert self.cli.process_input("exit") is False

    @patch('builtins.print')
    def test_process_input_help(self, mock_print):
        """Test help command."""
        result = self.cli.process_input("help")
        assert result is True
        mock_print.assert_called()

    def test_process_input_empty(self):
        """Test empty input."""
        assert self.cli.process_input("") is True
        assert self.cli.process_input("   ") is True

    @patch('builtins.print')
    def test_process_input_calculation(self, mock_print):
        """Test calculation input."""
        result = self.cli.process_input("5 + 3")
        assert result is True
        mock_print.assert_called_with("Result: 8")

    @patch('builtins.print')
    def test_process_input_invalid_input(self, mock_print):
        """Test invalid input handling."""
        result = self.cli.process_input("abc + def")
        assert result is True
        # Check that error message was printed
        assert any("Input Error" in str(call) for call in mock_print.call_args_list)

    @patch('builtins.print')
    def test_process_input_division_by_zero(self, mock_print):
        """Test division by zero handling."""
        result = self.cli.process_input("5 / 0")
        assert result is True
        # Check that error message was printed
        assert any("Math Error" in str(call) for call in mock_print.call_args_list)

    @patch('builtins.input', side_effect=['5 + 3', 'quit'])
    @patch('builtins.print')
    def test_run_with_calculation_and_quit(self, mock_print, mock_input):
        """Test run method with calculation and quit."""
        self.cli.run()
        # Verify that calculation result was printed
        result_calls = [call for call in mock_print.call_args_list if "Result: 8" in str(call)]
        assert len(result_calls) > 0

    @patch('builtins.input', side_effect=KeyboardInterrupt())
    @patch('builtins.print')
    def test_run_keyboard_interrupt(self, mock_print, mock_input):
        """Test keyboard interrupt handling."""
        with pytest.raises(SystemExit):
            self.cli.run()

    @patch('builtins.input', side_effect=EOFError())
    @patch('builtins.print')
    def test_run_eof_error(self, mock_print, mock_input):
        """Test EOF error handling."""
        self.cli.run()
        # Check that goodbye message was printed
        assert any("Goodbye" in str(call) for call in mock_print.call_args_list)

    @patch('builtins.print')
    def test_process_input_invalid_operation(self, mock_print):
        """Test invalid operation handling."""
        # Need to mock the validator to allow the input through to the calculator
        with patch.object(self.cli.validator, 'parse_calculation_input') as mock_parse:
            from calculator.exceptions import InvalidOperationError
            mock_parse.return_value = (5, "@", 3)
            # Mock calculator to raise InvalidOperationError
            with patch.object(self.cli.calculator, 'calculate') as mock_calc:
                mock_calc.side_effect = InvalidOperationError("Invalid operation: @")
                result = self.cli.process_input("5 @ 3")
                assert result is True
                # Check that error message was printed
                assert any("Operation Error" in str(call) for call in mock_print.call_args_list)

    @patch('builtins.print')  
    def test_process_input_overflow_error(self, mock_print):
        """Test overflow error handling."""
        # This should trigger overflow in operations
        result = self.cli.process_input("1e308 + 1e308")
        assert result is True
        # Check that error message was printed
        assert any("Overflow Error" in str(call) for call in mock_print.call_args_list)

    @patch('builtins.print')
    def test_process_input_unexpected_error(self, mock_print):
        """Test unexpected error handling."""
        # Mock validator to raise unexpected exception
        with patch.object(self.cli.validator, 'parse_calculation_input') as mock_parse:
            mock_parse.side_effect = RuntimeError("Unexpected error")
            
            result = self.cli.process_input("5 + 3")
            assert result is True
            # Check that error message was printed
            assert any("Unexpected error" in str(call) for call in mock_print.call_args_list)

    @patch('builtins.input', side_effect=Exception("Test exception"))
    @patch('builtins.print')
    def test_run_unexpected_exception(self, mock_print, mock_input):
        """Test unexpected exception in main loop."""
        with pytest.raises(SystemExit):
            self.cli.run()

    @patch('builtins.print')
    def test_process_input_calculator_error(self, mock_print):
        """Test calculator error handling."""
        from calculator.exceptions import CalculatorError
        with patch.object(self.cli.validator, 'parse_calculation_input') as mock_parse:
            mock_parse.return_value = (5, "+", 3)
            with patch.object(self.cli.calculator, 'calculate') as mock_calc:
                mock_calc.side_effect = CalculatorError("Calculator error")
                result = self.cli.process_input("5 + 3")
                assert result is True
                assert any("Calculator Error" in str(call) for call in mock_print.call_args_list)
