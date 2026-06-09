import flet as ft
from app.services.task_service import TaskService

class TodoApp:
    def __init__(self, page: ft.Page, service: TaskService) -> None:
        self.page = page
        self.service = service

    def render(self):
        pass

    def refresh_tasks(self):
        pass
