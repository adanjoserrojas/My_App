"""Tests for the RANDOM_BINARIES array declared in config.py."""
import importlib


def test_import_random_binaries():
    """Importing RANDOM_BINARIES from config succeeds without error."""
    from config import RANDOM_BINARIES  # noqa: F401


def test_random_binaries_is_list():
    from config import RANDOM_BINARIES
    assert isinstance(RANDOM_BINARIES, list), "RANDOM_BINARIES must be a list"


def test_random_binaries_has_five_elements():
    from config import RANDOM_BINARIES
    assert len(RANDOM_BINARIES) == 5, f"Expected 5 elements, got {len(RANDOM_BINARIES)}"


def test_each_element_is_integer():
    """Each element should be an int (binary literals are ints in Python)."""
    from config import RANDOM_BINARIES
    for i, val in enumerate(RANDOM_BINARIES):
        assert isinstance(val, int), f"Element {i} is not an int: {val!r}"


def test_each_element_is_non_negative():
    """Binary values should be non-negative."""
    from config import RANDOM_BINARIES
    for i, val in enumerate(RANDOM_BINARIES):
        assert val >= 0, f"Element {i} is negative: {val}"


def test_each_element_has_valid_binary_representation():
    """Each value can be expressed as a binary string starting with '0b'."""
    from config import RANDOM_BINARIES
    for i, val in enumerate(RANDOM_BINARIES):
        bin_str = bin(val)
        assert bin_str.startswith("0b"), f"Element {i} binary repr invalid: {bin_str}"
        # The digits after '0b' should only be 0s and 1s
        digits = bin_str[2:]
        assert all(c in "01" for c in digits), f"Element {i} has unexpected binary digits: {digits}"


def test_existing_config_attributes_preserved():
    """Existing config.py attributes must still be accessible."""
    import config
    assert hasattr(config, "BASE_DIR")
    assert hasattr(config, "DATA_FILE")
    assert hasattr(config, "DEBUG")
    assert hasattr(config, "SECRET_KEY")
