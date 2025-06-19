# my_server_app/app/core/exceptions.py

# This file defines custom exception classes for the application.
# Basic imports would go here if needed for custom exceptions.

# Define custom exception classes for the application.

class CustomException(Exception):
    """Base custom exception."""
    pass

class ItemNotFoundException(CustomException):
    """Exception raised when an item is not found."""
    def __init__(self, item_id: int):
        self.item_id = item_id
        super().__init__(f"Item with id {item_id} not found")

class InvalidInputException(CustomException):
    """Exception raised for invalid input data."""
    def __init__(self, detail: str):
        self.detail = detail
        super().__init__(f"Invalid input: {detail}")

# Add more custom exceptions as needed for specific scenarios