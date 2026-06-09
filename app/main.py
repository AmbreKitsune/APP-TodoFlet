import flet as ft
from app.models.task import Task
from app.services.task_service import TaskService


def application(page: ft.Page):
    page.title = "Todo App"

    page.window.width = 600
    page.window.height = 400


if __name__ == "__main__":
    service = TaskService()
    task1 = service.add_task(title="Купить хлеб")
    task2 = service.add_task(title="Купить колу")
    print(service.get_tasks())
    service.delete_task(task_id=task1.id) 
    print(service.get_tasks())

    ft.run(application)
