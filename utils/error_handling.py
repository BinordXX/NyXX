import logging
import sys
import traceback

# Set up basic logging configuration
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

class CustomError(Exception):
    """Base class for custom exceptions in the NyXX system."""
    pass

class InvalidConfigurationError(CustomError):
    """Raised when there is an invalid configuration."""
    pass

class DataProcessingError(CustomError):
    """Raised when an error occurs during data processing."""
    pass

class AgentError(CustomError):
    """Raised when an error is specific to an agent's operations."""
    pass

class SystemError(CustomError):
    """A general system-level error."""
    pass

def handle_error(error: Exception):
    """
    Centralized function to handle and log errors.
    Logs the error with traceback for debugging.
    """
    error_type = type(error).__name__
    logging.error(f"Error Type: {error_type}")
    logging.error(f"Error Message: {str(error)}")
    logging.error("Stack Trace:")
    logging.error("".join(traceback.format_tb(error.__traceback__)))

    # In case of critical errors, we could potentially terminate the system or initiate a fail-safe
    if isinstance(error, SystemError):
        logging.critical("A system error has occurred. Shutting down.")
        sys.exit(1)  # Exit with a non-zero code to indicate failure

def example_function_that_might_fail():
    """
    An example function that might raise different types of errors.
    """
    try:
        # Simulate a specific error
        raise DataProcessingError("The data format is incorrect.")
    except CustomError as e:
        handle_error(e)

# Example of triggering an error for demonstration
if __name__ == "__main__":
    try:
        example_function_that_might_fail()
    except Exception as e:
        handle_error(e)
