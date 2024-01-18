from flask import Flask, request
from repositories.task import TaskRepository

app = Flask(__name__)

task_repository = TaskRepository()


@app.route("/tasks", methods=("POST",))
def create_task():
    data = request.get_json()
    task = task_repository.create(
        title=data.get("title"), description=data.get("description")
    )
    return task.to_dict(), 201


@app.route("/tasks", methods=("GET",))
def get_tasks():
    tasks = [task.to_dict() for task in task_repository.get_all()]
    return {"tasks": tasks, "total_tasks": len(tasks)}, 200


@app.route("/tasks/<int:task_id>", methods=("GET",))
def get_task(task_id):
    task = task_repository.get_by_id(task_id)
    if task:
        return task.to_dict(), 200
    return {"message": "Task not found"}, 404


@app.route("/tasks/<int:task_id>", methods=("PUT",))
def update_task(task_id):
    data = request.get_json()
    task = task_repository.update(
        task_id=task_id,
        title=data.get("title"),
        description=data.get("description"),
        completed=data.get("completed"),
    )
    if task:
        return task.to_dict(), 200
    return {"message": "Task not found"}, 404


@app.route("/tasks/<int:task_id>", methods=("DELETE",))
def delete_task(task_id):
    if task_repository.delete(task_id):
        return "", 204
    return {"message": "Task not found"}, 404
