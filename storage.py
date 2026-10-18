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
