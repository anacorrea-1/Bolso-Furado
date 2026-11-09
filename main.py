import flet as ft

from src.view.login_view import LoginUsuarioView

def main (page: ft.Page):
    tela_cadastro_usuario = LoginUsuarioView(page)
    page.views = [tela_cadastro_usuario]

ft.run(main)