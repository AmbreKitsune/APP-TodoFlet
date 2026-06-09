import flet as ft


def application(page: ft.Page):
    page.title = "Todo"
    
    page.window.width = 600
    page.window.height = 400

    page.theme_mode = ft.ThemeMode.DARK

    page.window.resizable = True
