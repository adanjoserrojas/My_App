"""Comprehensive test-suite for the library package.

Run with:  pytest library/test_library.py -v
"""

import pytest

from library import (
    Book,
    LibraryManager,
    BookNotFoundError,
    BookNotRentedError,
    BookUnavailableError,
    DuplicateBookError,
)


# ---------------------------------------------------------------------------
# Book unit tests
# ---------------------------------------------------------------------------

class TestBook:
    def test_attributes(self):
        b = Book("Clean Code", "Robert C. Martin", 29.99, "978-0132350884")
        assert b.title == "Clean Code"
        assert b.author == "Robert C. Martin"
        assert b.price == 29.99
        assert b.isbn == "978-0132350884"
        assert b.status == Book.AVAILABLE

    def test_repr(self):
        b = Book("Clean Code", "Robert C. Martin", 29.99, "978-0132350884")
        r = repr(b)
        assert "Clean Code" in r
        assert "978-0132350884" in r

    def test_eq_same_isbn(self):
        b1 = Book("A", "Author", 10.0, "ISBN-1")
        b2 = Book("B", "Other", 20.0, "ISBN-1")
        assert b1 == b2

    def test_eq_different_isbn(self):
        b1 = Book("A", "Author", 10.0, "ISBN-1")
        b2 = Book("A", "Author", 10.0, "ISBN-2")
        assert b1 != b2

    def test_eq_not_a_book(self):
        b = Book("A", "Author", 10.0, "ISBN-1")
        assert b != "ISBN-1"

    def test_hash_same_isbn(self):
        b1 = Book("A", "X", 1.0, "ISBN-1")
        b2 = Book("B", "Y", 2.0, "ISBN-1")
        assert hash(b1) == hash(b2)


# ---------------------------------------------------------------------------
# LibraryManager – add / delete / list
# ---------------------------------------------------------------------------

class TestAddDeleteList:
    def setup_method(self):
        self.mgr = LibraryManager()
        self.book = Book("Refactoring", "Martin Fowler", 44.99, "978-0201485677")

    def test_add_and_list(self):
        self.mgr.add_book(self.book)
        books = self.mgr.list_books()
        assert len(books) == 1
        assert books[0] is self.book

    def test_add_duplicate_raises(self):
        self.mgr.add_book(self.book)
        with pytest.raises(DuplicateBookError):
            self.mgr.add_book(Book("Other", "Other", 9.99, self.book.isbn))

    def test_delete_existing(self):
        self.mgr.add_book(self.book)
        self.mgr.delete_book(self.book.isbn)
        assert self.mgr.list_books() == []

    def test_delete_missing_raises(self):
        with pytest.raises(BookNotFoundError):
            self.mgr.delete_book("nonexistent")

    def test_list_empty(self):
        assert self.mgr.list_books() == []

    def test_list_multiple(self):
        b2 = Book("Design Patterns", "GoF", 39.99, "978-0201633610")
        self.mgr.add_book(self.book)
        self.mgr.add_book(b2)
        assert len(self.mgr.list_books()) == 2


# ---------------------------------------------------------------------------
# Renting
# ---------------------------------------------------------------------------

class TestRentReturn:
    def setup_method(self):
        self.mgr = LibraryManager()
        self.book = Book("TDD", "Kent Beck", 34.99, "978-0321146533")
        self.mgr.add_book(self.book)

    def test_rent_available(self):
        self.mgr.rent_book(self.book.isbn)
        assert self.book.status == Book.RENTED

    def test_rent_already_rented_raises(self):
        self.mgr.rent_book(self.book.isbn)
        with pytest.raises(BookUnavailableError):
            self.mgr.rent_book(self.book.isbn)

    def test_rent_reserved_raises(self):
        self.mgr.reserve_book(self.book.isbn)
        with pytest.raises(BookUnavailableError):
            self.mgr.rent_book(self.book.isbn)

    def test_rent_missing_raises(self):
        with pytest.raises(BookNotFoundError):
            self.mgr.rent_book("no-such-isbn")

    def test_return_rented(self):
        self.mgr.rent_book(self.book.isbn)
        self.mgr.return_book(self.book.isbn)
        assert self.book.status == Book.AVAILABLE

    def test_return_not_rented_raises(self):
        with pytest.raises(BookNotRentedError):
            self.mgr.return_book(self.book.isbn)

    def test_return_reserved_raises(self):
        self.mgr.reserve_book(self.book.isbn)
        with pytest.raises(BookNotRentedError):
            self.mgr.return_book(self.book.isbn)

    def test_return_missing_raises(self):
        with pytest.raises(BookNotFoundError):
            self.mgr.return_book("no-such-isbn")


# ---------------------------------------------------------------------------
# Reserving
# ---------------------------------------------------------------------------

class TestReserve:
    def setup_method(self):
        self.mgr = LibraryManager()
        self.book = Book("DDD", "Eric Evans", 54.99, "978-0321125217")
        self.mgr.add_book(self.book)

    def test_reserve_available(self):
        self.mgr.reserve_book(self.book.isbn)
        assert self.book.status == Book.RESERVED

    def test_reserve_already_reserved_raises(self):
        self.mgr.reserve_book(self.book.isbn)
        with pytest.raises(BookUnavailableError):
            self.mgr.reserve_book(self.book.isbn)

    def test_reserve_rented_raises(self):
        self.mgr.rent_book(self.book.isbn)
        with pytest.raises(BookUnavailableError):
            self.mgr.reserve_book(self.book.isbn)

    def test_reserve_missing_raises(self):
        with pytest.raises(BookNotFoundError):
            self.mgr.reserve_book("no-such-isbn")


# ---------------------------------------------------------------------------
# Pricing
# ---------------------------------------------------------------------------

class TestGetPrice:
    def setup_method(self):
        self.mgr = LibraryManager()
        self.book = Book("SICP", "Abelson & Sussman", 65.00, "978-0262510875")
        self.mgr.add_book(self.book)

    def test_get_price(self):
        assert self.mgr.get_price(self.book.isbn) == 65.00

    def test_get_price_missing_raises(self):
        with pytest.raises(BookNotFoundError):
            self.mgr.get_price("no-such-isbn")


# ---------------------------------------------------------------------------
# Exception hierarchy
# ---------------------------------------------------------------------------

class TestExceptionHierarchy:
    """All custom exceptions should be catchable as LibraryError."""

    def test_book_not_found_is_library_error(self):
        assert issubclass(BookNotFoundError, Exception)
        from library import LibraryError
        assert issubclass(BookNotFoundError, LibraryError)

    def test_duplicate_is_library_error(self):
        from library import LibraryError
        assert issubclass(DuplicateBookError, LibraryError)

    def test_unavailable_is_library_error(self):
        from library import LibraryError
        assert issubclass(BookUnavailableError, LibraryError)

    def test_not_rented_is_library_error(self):
        from library import LibraryError
        assert issubclass(BookNotRentedError, LibraryError)
