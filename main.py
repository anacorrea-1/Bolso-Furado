import flet as ft

from src.view.login_view import LoginUsuarioView
from src.view.cadastro import CadastroUsuarioView

def main (page: ft.Page):
    tela_login_usuario = LoginUsuarioView(page)
    tela_cadastro_usuario = CadastroUsuarioView(page)

    def route(e = None):
        page.views.clear()

        if page.route == "/cadastro":
            page.views.append (tela_cadastro_usuario)
            
        elif page.route == "/login":
            page.views.append (tela_login_usuario)
        
        page.update()

    page.on_route_change = route
    route()

    page.views.append (tela_login_usuario)

ft.run(main)