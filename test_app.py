
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
    response = client.post(
        "/add",
        data={"task": "Complete DevOps project", "priority": "high"},
    )
    assert response.status_code == 302
    assert todo_app.tasks[0]["name"] == "Complete DevOps project"
    assert todo_app.tasks[0]["priority"] == "high"
    assert todo_app.tasks[0]["completed"] is False


def test_delete_task():
    todo_app.tasks.append({
        "name": "Test task",
        "priority": "medium",
        "completed": False,
    })
    client = todo_app.app.test_client()
    response = client.post("/delete/0")
    assert response.status_code == 302
    assert len(todo_app.tasks) == 0


def test_complete_task():
    todo_app.tasks.append({
        "name": "Finish testing",
        "priority": "high",
        "completed": False,
    })
    client = todo_app.app.test_client()
    response = client.post("/complete/0")
    assert response.status_code == 302
    assert todo_app.tasks[0]["completed"] is True


def test_filter_completed_tasks():
    todo_app.tasks.extend([
        {"name": "Pending task", "priority": "low", "completed": False},
        {"name": "Finished task", "priority": "high", "completed": True},
    ])
    client = todo_app.app.test_client()
    response = client.get("/?status=completed")
    assert b"Finished task" in response.data
    assert b"Pending task" not in response.data
