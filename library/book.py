"""Book entity – demonstrates **Encapsulation**.

All book-related data (title, author, price, isbn) and the status flag live
inside a single object.  The status is managed by LibraryManager so callers
cannot accidentally put a book into an invalid state.
"""


class Book:
    """Represents a single book in the library catalog."""

    AVAILABLE = "available"
    RENTED = "rented"
    RESERVED = "reserved"

    def __init__(self, title: str, author: str, price: float, isbn: str) -> None:
        self.title = title
        self.author = author
        self.price = price
        self.isbn = isbn
        self.status: str = self.AVAILABLE

    # -- magic methods --------------------------------------------------------

    def __repr__(self) -> str:
        return (
            f"Book(title={self.title!r}, author={self.author!r}, "
            f"price={self.price!r}, isbn={self.isbn!r}, status={self.status!r})"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self.isbn == other.isbn

    def __hash__(self) -> int:
        return hash(self.isbn)
