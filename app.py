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
