import flet as ft

from app.services.task_service import TaskService


class TodoApp:
    def __init__(self, page: ft.Page, service: TaskService) -> None:
        self.page = page
        self.service = service

    def render(self):
        column_layout = ft.Column(
            controls=[
                ft.Text("Todo App"),
                ft.TextField(label="Введите текст"),
                ft.ElevatedButton("Добавить задачу"),
                ft.Text("Счётчик задачи: 0")
            ]
        )

        task_list = ft.Column(
            controls=[
                ft.Text("Задач пока нет")
            ]
        )

        self.page.add(column_layout, task_list)
        self.page.update()

    def refresh_tasks(self):
        pass
