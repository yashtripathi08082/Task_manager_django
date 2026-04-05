import pytest
from tasks.models import Task

# -------------------------------
# TEST CREATE TASK (API)
# -------------------------------
@pytest.mark.django_db
def test_create_task_api(client):
    data = {
        "title": "Test Task",
        "description": "Testing create",
        "due_date": "2026-04-20",
        "status": "Pending"
    }

    response = client.post(
        "/add/",
        data=data,
        content_type="application/json"
    )

    assert response.status_code == 200
    assert Task.objects.count() == 1
    assert Task.objects.first().title == "Test Task"


# -------------------------------
# TEST GET TASKS (API JSON)
# -------------------------------
@pytest.mark.django_db
def test_get_tasks_api(client):
    Task.objects.create(
        title="Task1",
        description="Test",
        due_date="2026-04-20",
        status="Pending"
    )

    response = client.get("/", HTTP_ACCEPT="application/json")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "Task1"


# -------------------------------
# TEST UPDATE TASK (API)
# -------------------------------
@pytest.mark.django_db
def test_update_task_api(client):
    task = Task.objects.create(
        title="Old Title",
        description="Old Desc",
        due_date="2026-04-20",
        status="Pending"
    )

    updated_data = {
        "title": "New Title",
        "description": "Updated Desc",
        "due_date": "2026-04-25",
        "status": "Completed"
    }

    response = client.put(
        f"/update/{task.id}/",
        data=updated_data,
        content_type="application/json"
    )

    task.refresh_from_db()

    assert response.status_code == 200
    assert task.title == "New Title"
    assert task.status == "Completed"


# -------------------------------
# TEST DELETE TASK (API)
# -------------------------------
@pytest.mark.django_db
def test_delete_task_api(client):
    task = Task.objects.create(
        title="Delete Me",
        description="Test",
        due_date="2026-04-20",
        status="Pending"
    )

    response = client.delete(f"/delete/{task.id}/")

    assert response.status_code == 200
    assert Task.objects.count() == 0


# -------------------------------
# TEST UI (OPTIONAL BONUS)
# -------------------------------
@pytest.mark.django_db
def test_task_page_ui(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Task List" in response.content