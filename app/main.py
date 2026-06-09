import flet as ft

def application(page: ft.Page):
    page.title = "Todo App"

    page.window.width = 600
    page.window.height = 400


ft.run(application)
