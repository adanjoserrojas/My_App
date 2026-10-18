import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Where tasks are saved. Override with the TODO_DATA_FILE environment variable.
DATA_FILE = os.environ.get("TODO_DATA_FILE", os.path.join(BASE_DIR, "tasks.json"))

DEBUG = os.environ.get("FLASK_DEBUG", "1") == "1"

# Secret key for session signing; set TODO_SECRET_KEY in production.
SECRET_KEY = os.environ.get("TODO_SECRET_KEY", "dev-secret-key")
