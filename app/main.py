import flet as ft
from app.ui.todo_app import TodoApp
from app.services.task_service import TaskService
from app.storage.json_task_storage import JsonTaskStorage


def application(page: ft.Page):
    page.title = "Todo App"

    page.window.width = 600
    page.window.height = 400


if __name__ == "__main__":
    storage = JsonTaskStorage()
    service = TaskService(storage)

    application = TodoApp(ft.Page, service)

    ft.run(TodoApp(service))
