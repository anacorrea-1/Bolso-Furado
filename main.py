import flet as ft

from src.view.login_view import LoginUsuarioView
from src.view.cadastro import CadastroUsuarioView
from src.view.conheca_view import ConhecaOAPP
from src.view.cadastro_categoria import CadastroCategoriaoView

# Paleta de Cores "Bolso Furado" 
COR_PRIMARIA = "#004D40"   
COR_DESTAQUE = "#F9A826"   
COR_TEXTO = "#263238"      
COR_FUNDO = "#F1F4F8"      
COR_CARTAO = "#FAFBFB"
COR_BORDA = "#E0E6ED"

def main(page:ft.Page):

    async def navegacao( e = None ):
        indice_clicado = e.control.selected_index

        if indice_clicado == 0:
            tela_login_usuario = LoginUsuarioView(page)
            await page.push_route("/conheca")

        elif indice_clicado == 1:
            tela_cadastro_categoria = CadastroCategoriaoView(page)
            await page.push_route("/cadcate")

        elif indice_clicado == 2:
            await page.push_route("")

        elif indice_clicado == 3:
            await page.push_route("")

        elif indice_clicado == 4:
            await page.push_route("")

        elif indice_clicado == 5:
            await page.push_route("/login")

    # Definição da NavigationBar
    navigation_bar = ft.NavigationBar(
        on_change=navegacao,
        selected_index=0,
        bgcolor=COR_CARTAO,
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.HOME_OUTLINED,
                selected_icon=ft.Icons.HOME,
                label="Início",
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.ASSIGNMENT_ADD,
                selected_icon=ft.Icons.ASSIGNMENT_ADD,
                label="Cadastrar categorias",
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.ADD_SHOPPING_CART_OUTLINED,
                selected_icon=ft.Icons.ADD_SHOPPING_CART_OUTLINED,
                label="Cadastrar despesa",
            ),

            ft.NavigationBarDestination(
                icon=ft.Icons.SHOPPING_BAG,
                selected_icon=ft.Icons.SHOPPING_BAG,
                label="Todas as despesas",
            ),

            ft.NavigationBarDestination(
                icon=ft.Icons.SHOPPING_CART_CHECKOUT,
                selected_icon=ft.Icons.SHOPPING_CART_CHECKOUT,
                label="Despesas por categorias",
            ),

            ft.NavigationBarDestination(
                icon=ft.Icons.EXIT_TO_APP,
                label="Sair",
            ),
        ],
    )


    def route(e = None):
        page.views.clear()

        if page.route == "/cadastro":
            tela_cadastro_usuario = CadastroUsuarioView(page)
            page.views.append(tela_cadastro_usuario)
            
        elif page.route == "/login":
            tela_login_usuario = LoginUsuarioView(page)
            page.views.append(tela_login_usuario)


        elif page.route == "/conheca":
                tela_conheca = ConhecaOAPP(page)
                tela_conheca.navigation_bar = navigation_bar
                page.views.append(tela_conheca)
        
        elif page.route == "/cadcate":
            tela_cadastro_categoria = CadastroCategoriaoView(page)
            tela_cadastro_categoria.navigation_bar = navigation_bar
            page.views.append(tela_cadastro_categoria)
            
        page.update()

    page.on_route_change = route
    route()

    page.navigate ("/login")

ft.run(main)