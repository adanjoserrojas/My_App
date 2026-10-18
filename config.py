import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Where tasks are saved. Override with the TODO_DATA_FILE environment variable.
DATA_FILE = os.environ.get("TODO_DATA_FILE", os.path.join(BASE_DIR, "tasks.json"))

DEBUG = os.environ.get("FLASK_DEBUG", "1") == "1"

# Secret key for session signing; set TODO_SECRET_KEY in production.
SECRET_KEY = os.environ.get("TODO_SECRET_KEY", "dev-secret-key")

# Array of 5 random binary values.
RANDOM_BINARIES = [0b1010, 0b1101, 0b0111, 0b10011, 0b11010]

x = 5
