"""Library Book Management System – an OOP demo.

Key OOP concepts illustrated:
* **Encapsulation** – Book wraps its data behind a clean attribute interface;
  LibraryManager hides the internal catalog dict from callers.
* **Abstraction** – consumers interact with high-level methods (add_book,
  rent_book, …) without worrying about how books are stored or how status
  transitions work.
* **Polymorphism** – custom exception hierarchy lets callers catch a common
  LibraryError *or* specific sub-types.
* **Inheritance** – every custom exception inherits from LibraryError,
  demonstrating the IS-A relationship.
"""

from library.book import Book
from library.exceptions import (
    LibraryError,
    BookNotFoundError,
    BookUnavailableError,
    BookNotRentedError,
    DuplicateBookError,
)
from library.library_manager import LibraryManager

__all__ = [
    "Book",
    "LibraryManager",
    "LibraryError",
    "BookNotFoundError",
    "BookUnavailableError",
    "BookNotRentedError",
    "DuplicateBookError",
]
