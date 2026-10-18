"""LibraryManager – demonstrates **Abstraction** and **Encapsulation**.

The internal `_catalog` dictionary is hidden; every mutation goes through a
public method that validates preconditions and raises descriptive errors.
"""

from __future__ import annotations

from typing import Dict, List

from library.book import Book
from library.exceptions import (
    BookNotFoundError,
    BookNotRentedError,
    BookUnavailableError,
    DuplicateBookError,
)


class LibraryManager:
    """High-level façade for managing a library catalog."""

    def __init__(self) -> None:
        self._catalog: Dict[str, Book] = {}

    # -- helpers --------------------------------------------------------------

    def _get_book(self, isbn: str) -> Book:
        """Return the Book for *isbn* or raise BookNotFoundError."""
        try:
            return self._catalog[isbn]
        except KeyError:
            raise BookNotFoundError(f"No book with ISBN {isbn!r} in catalog.")

    # -- public API -----------------------------------------------------------

    def add_book(self, book: Book) -> None:
        """Add *book* to the catalog.

        Raises DuplicateBookError if a book with the same ISBN already exists.
        """
        if book.isbn in self._catalog:
            raise DuplicateBookError(
                f"A book with ISBN {book.isbn!r} already exists."
            )
        self._catalog[book.isbn] = book

    def delete_book(self, isbn: str) -> None:
        """Remove the book identified by *isbn*.

        Raises BookNotFoundError if the ISBN is not in the catalog.
        """
        self._get_book(isbn)  # validates existence
        del self._catalog[isbn]

    def rent_book(self, isbn: str) -> None:
        """Mark the book as rented.

        Raises BookNotFoundError if missing.
        Raises BookUnavailableError if the book is already rented or reserved.
        """
        book = self._get_book(isbn)
        if book.status != Book.AVAILABLE:
            raise BookUnavailableError(
                f"Book {isbn!r} is currently {book.status} and cannot be rented."
            )
        book.status = Book.RENTED

    def return_book(self, isbn: str) -> None:
        """Return a rented book, setting its status back to available.

        Raises BookNotFoundError if missing.
        Raises BookNotRentedError if the book is not currently rented.
        """
        book = self._get_book(isbn)
        if book.status != Book.RENTED:
            raise BookNotRentedError(
                f"Book {isbn!r} is not currently rented (status={book.status!r})."
            )
        book.status = Book.AVAILABLE

    def reserve_book(self, isbn: str) -> None:
        """Reserve an available book.

        Raises BookNotFoundError if missing.
        Raises BookUnavailableError if the book is already rented or reserved.
        """
        book = self._get_book(isbn)
        if book.status != Book.AVAILABLE:
            raise BookUnavailableError(
                f"Book {isbn!r} is currently {book.status} and cannot be reserved."
            )
        book.status = Book.RESERVED

    def get_price(self, isbn: str) -> float:
        """Return the price of the book with the given *isbn*.

        Raises BookNotFoundError if the ISBN is absent.
        """
        return self._get_book(isbn).price

    def list_books(self) -> List[Book]:
        """Return a list of every Book currently in the catalog."""
        return list(self._catalog.values())
