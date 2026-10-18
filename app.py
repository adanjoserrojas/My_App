from flask import Flask, jsonify, render_template, request

import config
from storage import load_tasks, save_tasks

app = Flask(__name__)
app.config["DATA_FILE"] = config.DATA_FILE


def get_tasks():
    return load_tasks(app.config["DATA_FILE"])


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/tasks")
def list_tasks():
    return jsonify(get_tasks())


@app.get("/tasks/<int:task_id>")
def get_task(task_id):
    task = next((t for t in get_tasks() if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task)


@app.post("/tasks")
def create_task():
    data = request.get_json(silent=True) or {}
    title = str(data.get("title", "")).strip()
    if not title:
        return jsonify({"error": "'title' is required"}), 400

    tasks = get_tasks()
    next_id = max((t["id"] for t in tasks), default=0) + 1
    task = {"id": next_id, "title": title, "done": bool(data.get("done", False))}
    tasks.append(task)
    save_tasks(app.config["DATA_FILE"], tasks)
    return jsonify(task), 201


if __name__ == "__main__":
    app.run(debug=config.DEBUG)
