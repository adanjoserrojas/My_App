"""Custom exception hierarchy – demonstrates **Inheritance** & **Polymorphism**.

All exceptions derive from a common `LibraryError` base class, so consumers
can handle them generically *or* specifically.
"""


class LibraryError(Exception):
    """Base exception for all library-related errors."""


class BookNotFoundError(LibraryError):
    """Raised when a requested ISBN does not exist in the catalog."""


class DuplicateBookError(LibraryError):
    """Raised when trying to add a book whose ISBN is already present."""


class BookUnavailableError(LibraryError):
    """Raised when trying to rent or reserve a book that is not available."""


class BookNotRentedError(LibraryError):
    """Raised when trying to return a book that is not currently rented."""
