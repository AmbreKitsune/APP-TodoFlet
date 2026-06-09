import flet as ft

from app.services.task_service import TaskService


class TodoApp:
    def __init__(self, page: ft.Page, service: TaskService) -> None:
        self.page = page
        self.service = service

    def render(self):
        self.task_input = ft.TextField(label="Введите текст")
        self.counter_text = ft.Text("Всего задач: 0")
        self.task_list = ft.Column(controls=[ft.Text("Задач пока нет")])

        column_layout = ft.Column(
            controls=[
                ft.Text("Todo App"),
                self.task_input,
                ft.ElevatedButton("Добавить задачу"),
                self.counter_text
            ]
        )

        self.page.add(column_layout, self.task_list)
        self.refresh_tasks()
        self.page.update()

    def refresh_tasks(self):
        tasks = self.service.get_tasks()
        self.task_list.controls.clear()
        self.counter_text.value = f"Всего задач: {len(tasks)}"

        if not tasks:
            self.task_list.controls.append(ft.Text("Задач пока нет"))
        else:
            for item in tasks:
                self.task_list.controls.append(ft.Text(item.title))

        self.page.update()

