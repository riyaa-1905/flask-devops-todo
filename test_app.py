
import app as todo_app


def setup_function():
    todo_app.tasks.clear()


def test_home_page():
    client = todo_app.app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"My DevOps To-Do App" in response.data


def test_add_task():
    client = todo_app.app.test_client()
    response = client.post("/add", data={"task": "Complete DevOps project"})
    assert response.status_code == 302
    assert "Complete DevOps project" in todo_app.tasks


def test_delete_task():
    todo_app.tasks.append("Test task")
    client = todo_app.app.test_client()
    response = client.post("/delete/0")
    assert response.status_code == 302
    assert "Test task" not in todo_app.tasks
