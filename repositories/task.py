from models.task import Task


class TaskRepository:
    def __init__(self) -> None:
        self.__tasks = []
        self.__last_id = 0

    def create(self, title: str, description: str) -> Task:
        self.__last_id += 1
        task = Task(id=self.__last_id, title=title, description=description)
        self.__tasks.append(task)
        return task

    def get_all(self) -> list[Task]:
        return self.__tasks.copy()
