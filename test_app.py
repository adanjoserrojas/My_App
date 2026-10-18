import pytest

from app import app


@pytest.fixture
def client(tmp_path):
    app.config["DATA_FILE"] = str(tmp_path / "tasks.json")
    app.config["TESTING"] = True
    return app.test_client()


def test_list_starts_empty(client):
    res = client.get("/tasks")
    assert res.status_code == 200
    assert res.json == [] #


def test_create_and_read_task(client):
    res = client.post("/tasks", json={"title": "Buy milk"})
    assert res.status_code == 201
    assert res.json == {"id": 1, "title": "Buy milk", "done": False}

    assert client.get("/tasks/1").json["title"] == "Buy milk"
    assert len(client.get("/tasks").json) == 1


def test_create_requires_title(client):
    res = client.post("/tasks", json={"title": "   "})
    assert res.status_code == 400


def test_missing_task_returns_404(client):
    assert client.get("/tasks/99").status_code == 404


def test_ids_keep_increasing(client):
    client.post("/tasks", json={"title": "One"})
    res = client.post("/tasks", json={"title": "Two"})
    assert res.json["id"] == 2
