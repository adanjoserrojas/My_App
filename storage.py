import json
import os


def load_tasks(path):
    """Return the list of tasks saved at path, or an empty list if none exist yet."""
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_tasks(path, tasks):
    """Write tasks to path as JSON."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def calculate(a, b, operation):
    """Perform a basic arithmetic operation on two numbers.

    Parameters
    ----------
    a : int or float
        The first operand.
    b : int or float
        The second operand.
    operation : str
        One of ``"+"``, ``"-"``, ``"x"`` (multiply), or ``"%"`` (modulo).

    Returns
    -------
    int or float
        The result of the operation.

    Raises
    ------
    ZeroDivisionError
        If *operation* is ``"%"`` and *b* is zero.
    ValueError
        If *operation* is not one of the supported operators.
    """
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "x":
        return a * b
    elif operation == "%":
        if b == 0:
            raise ZeroDivisionError("Cannot perform modulo by zero")
        return a % b
    else:
        raise ValueError(f"Unsupported operation '{operation}'. Use '+', '-', 'x', or '%'.")


def print_addition():
    """Print the result of 4 + 4."""
    print(calculate(4, 4, "+"))
