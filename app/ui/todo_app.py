import flet as ft

from app.services.task_service import TaskService


class TodoApp:
    def __init__(self, page: ft.Page, service: TaskService) -> None:
        self.page = page
        self.service = service

    def render(self):
        self.task_input = ft.TextField(
            label="Новая задача",

            filled=True,
            bgcolor="#C6D6C7",
            color="#212121",

            focused_bgcolor="#257316",
            focused_border_color="#257316",
            focused_color="#257316", 

            expand=True
            )
        self.counter_text = ft.Text(
            "Всего задач: 0",
            size=24,
            weight=ft.FontWeight.BOLD
            )
        self.task_list = ft.Column(
            controls=[ft.Text("Задач пока нет")],
            )

        input_row_layout = ft.Row(
            controls=[
                self.task_input,
                ft.IconButton(
                    icon=ft.Icons.ADD_BOX,
                    bgcolor=ft.Colors.GREEN,
                    on_click=self.handle_add_task
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            margin=ft.Margin.only(left=10, right=10),
            spacing=20
        )

        container_list = ft.Container(
            expand=True,
            width=float("inf"),
            content=self.task_list,
            border=ft.Border.all(width=2, color="#FFFFFF"),
            padding=10
        )

        container_layout = ft.Column(
            controls=[
                ft.Text("Todo App", size=24, weight=ft.FontWeight.BOLD),
                input_row_layout,
                self.counter_text,
                container_list
            ]
        )

        self.page.add(container_layout)
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
                        ],
                        scroll=ft.ScrollMode.AUTO,
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        margin=10
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
