from flask import Flask, request
from repositories.task import TaskRepository

app = Flask(__name__)

task_repository = TaskRepository()


@app.route("/tasks", methods=("POST", "GET"))
def create_task():
    if request.method == "GET":
        return [task.to_dict() for task in task_repository.get_all()], 200
    data = request.get_json()
    task = task_repository.create(
        title=data.get("title"), description=data.get("description")
    )
    return task.to_dict(), 201
