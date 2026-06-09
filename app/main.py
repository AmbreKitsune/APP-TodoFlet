import flet as ft
from app.models.task import Task


def application(page: ft.Page):
    page.title = "Todo App"

    page.window.width = 600
    page.window.height = 400


if __name__ == "__main__":
    task = Task(id="1", title=" Купить хлеб ")
    print(task.model_dump())

    ft.run(application)
