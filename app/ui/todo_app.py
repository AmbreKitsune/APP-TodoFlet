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
                ft.ElevatedButton("Добавить задачу", on_click=self.handle_add_task),
                self.counter_text
            ]
        )

        self.page.add(column_layout, self.task_list)
        self.refresh_tasks()

    def refresh_tasks(self):
        tasks = self.service.get_tasks()
        self.task_list.controls.clear()
        self.counter_text.value = f"Всего задач: {len(tasks)}"

        if not tasks:
            self.task_list.controls.append(ft.Text("Задач пока нет"))
        else:
            for item in tasks:
                self.task_list.controls.append(
                    ft.Row(
                        controls=[
                            ft.Text(item.title),
                            ft.IconButton(icon=ft.Icons.DELETE_FOREVER, on_click=lambda e, task_id=item.id: self.handle_delete_task(task_id))
                        ]
                    )
                )

        self.page.update()

    def handle_add_task(self, e):
        title = self.task_input.value.strip()
        if not title:
            return
        
        self.service.add_task(title)
        self.task_input.value = ""
        self.refresh_tasks()

    def handle_delete_task(self, task_id: str):
        self.service.delete_task(task_id)
        self.refresh_tasks()
