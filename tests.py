import pytest
import requests


BASE_URL = "http://127.0.0.1:5000"
tasks = []


def test_create_task():
    new_task_data = {"title": "Test Task", "description": "Test Description"}
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 201
    assert response.json()["title"] == new_task_data["title"]
    assert response.json()["description"] == new_task_data["description"]
    assert "id" in response.json()
    assert response.json()["completed"] is False
    tasks.append(response.json()["id"])


def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    assert "tasks" in response.json()
    assert "total_tasks" in response.json()


def test_get_task():
    if tasks:
        response = requests.get(f"{BASE_URL}/tasks/{tasks[0]}")
        assert response.status_code == 200
        assert response.json()["id"] == tasks[0]


def test_update_task():
    if tasks:
        update_task_data = {
            "title": "Updated Test Task",
            "description": "Updated Test Description",
            "completed": True,
        }
        response = requests.put(f"{BASE_URL}/tasks/{tasks[0]}", json=update_task_data)
        assert response.status_code == 200
        assert response.json()["title"] == update_task_data["title"]
        assert response.json()["description"] == update_task_data["description"]
        assert response.json()["completed"] is True


def test_delete_task():
    if tasks:
        response = requests.delete(f"{BASE_URL}/tasks/{tasks[0]}")
        assert response.status_code == 204
        tasks.pop(0)
