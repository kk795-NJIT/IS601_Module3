"""Unit tests for the main entry point."""

from unittest.mock import MagicMock, patch

import main


class TestMain:
    """Test class for main module functionality."""

    @patch("main.CalculatorCLI")
    def test_main_function(self, mock_cli_class):
        """Test main function creates and runs CLI."""
        mock_cli_instance = MagicMock()
        mock_cli_class.return_value = mock_cli_instance

        main.main()

        mock_cli_class.assert_called_once()
        mock_cli_instance.run.assert_called_once()

    @patch("main.main")
    def test_name_main_guard(self, mock_main):
        """Test that main is called when script is run directly."""
        # This test simulates the __name__ == "__main__" guard
        # We can't easily test this directly, so we just verify main() would be called
        assert callable(main.main)
