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
