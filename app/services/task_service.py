from uuid import uuid4

from app.storage.json_task_storage import JsonTaskStorage
from app.models.task import Task


class TaskService:
    def __init__(self, storage: JsonTaskStorage) -> None:
        self.storage = storage

    def get_tasks(self) -> list[Task]:
        tasks = self.storage.load_tasks()
        return tasks

    def add_task(self, title: str) -> Task:
        tasks = self.storage.load_tasks()

        task_id = str(uuid4())
        task = Task(id=task_id, title=title)
        tasks.append(task)

        self.storage.save_tasks(tasks)

        return task

    def delete_task(self, task_id: str) -> None:
        old_tasks = self.storage.load_tasks()
        new_tasks = [item for item in old_tasks if item.id != task_id]
        self.storage.save_tasks(new_tasks)
