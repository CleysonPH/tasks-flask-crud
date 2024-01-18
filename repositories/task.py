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

    def get_by_id(self, task_id: int) -> Task | None:
        for task in self.__tasks:
            if task.id == task_id:
                return task
        return None

    def update(
        self, task_id: int, title: str, description: str, completed: bool
    ) -> Task | None:
        task = self.get_by_id(task_id)
        if task:
            task.title = title
            task.description = description
            task.completed = completed
        return task
