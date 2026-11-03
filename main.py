import flet as ft

from src.view.cadastro import CadastroUsuarioView

def main (page: ft.Page):
    tela_cadastro_usuario = CadastroUsuarioView(page)
    page.views = [tela_cadastro_usuario]

ft.run(main)