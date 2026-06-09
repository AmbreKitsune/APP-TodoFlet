import flet as ft
from app.models.task import Task
from app.storage.json_task_storage import JsonTaskStorage


def application(page: ft.Page):
    page.title = "Todo App"

    page.window.width = 600
    page.window.height = 400


if __name__ == "__main__":
    task = Task(id="1", title=" Купить хлеб ")
    print(task.model_dump())

    jps = JsonTaskStorage()
    print(jps.load_tasks())

    ft.run(application)
