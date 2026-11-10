import flet as ft

class ConhecaOAPP(ft.View):
    def __init__(self, _page: ft.Page):
        super().__init__()
        
        # Paleta de Cores "Bolso Furado" 
        self.COR_PRIMARIA = "#004D40"   
        self.COR_DESTAQUE = "#F9A826"   
        self.COR_TEXTO = "#263238"      
        self.COR_FUNDO = "#F1F4F8"      
        self.COR_CARTAO = "#FAFBFB"
        self.COR_BORDA = "#E0E6ED"

        # Configurações da View
        self.route = "/conheca" 
        self.bgcolor = self.COR_FUNDO
        self.padding = 0

        # Configurações globais da janela
        _page.title = "Bolso Furado - Conheça o App"
        _page.window.maximized = True

        async def teste(e=None):
                indice_clicado = e.control.selected_index

                if indice_clicado == 0:
                    await self.page.push_route("/conheca")

                elif indice_clicado == 1:
                    await self.page.push_route("")

                elif indice_clicado == 2:
                    await self.page.push_route("")

                elif indice_clicado == 3:
                    await self.page.push_route("")

                elif indice_clicado == 4:
                    await self.page.push_route("")



        # Definição da NavigationBar
        self.navigation_bar = ft.NavigationBar(
            on_change= teste,
            selected_index=0,
            bgcolor=self.COR_CARTAO,
            destinations=[
                ft.NavigationBarDestination(
                    icon=ft.Icons.HOME_OUTLINED,
                    selected_icon=ft.Icons.HOME,
                    label="Início",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.ASSIGNMENT_ADD,
                    selected_icon=ft.Icons.ASSIGNMENT_ADD,
                    label="Cadastrar por categorias",
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

        self.logo_app = ft.Image(
            src="src/view/img/logo.png",
            width=180,
            height=140,
            )

        # Banner de Título Superior 
        self.banner_titulo = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(ft.Icons.AUTO_AWESOME, color=self.COR_DESTAQUE, size=20),
                    ft.Text(
                        "Fechando as Brechas do Seu Orçamento",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color=self.COR_PRIMARIA,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            bgcolor=self.COR_CARTAO,
            padding=ft.Padding(left=25, top=10, right=25, bottom=10),
            border_radius=30,
            border=ft.Border.all(width=1, color=self.COR_BORDA),
            shadow=ft.BoxShadow(
                blur_radius=8,
                color="#0D000000",
                offset=ft.Offset(0, 2),
            ),
            max_width=520,
        )

        # Cartão Principal de História 
        self.cartao_historia = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=self.logo_app,
                        bgcolor="#FFF8E1",
                        padding=16,
                        border_radius=50,
                    ),
                    ft.Text(
                        "Como tudo começou...",
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        color=self.COR_PRIMARIA
                    ),
                    ft.Divider(color="#ECEFF1", height=20),
                    
                    ft.Text(
                        spans=[
                            ft.TextSpan("Era uma vez o "),
                            ft.TextSpan("Godofredo", ft.TextStyle(weight=ft.FontWeight.BOLD, color=self.COR_PRIMARIA)),
                            ft.TextSpan(", um sujeito trabalhador que no fim do mês sempre se fazia a mesma pergunta: "),
                            ft.TextSpan("'Para onde foi o meu dinheiro?'", ft.TextStyle(weight=ft.FontWeight.BOLD, color=self.COR_DESTAQUE)),
                            ft.TextSpan(". Ele recebia o seu salário, pagava as contas básicas e, quando assustava, o saldo na conta já tinha sumido misteriosamente em pequenas coxinhas no meio da tarde, cafés e gastos imperceptíveis. "),
                            ft.TextSpan("O seu bolso não tinha fundo... tinha um verdadeiro buraco!", ft.TextStyle(weight=ft.FontWeight.BOLD)),
                        ],
                        size=15,
                        color=self.COR_TEXTO,
                        text_align=ft.TextAlign.JUSTIFY,
                    ),
                    
                    ft.Container(height=8),
                    
                    ft.Text(
                        spans=[
                            ft.TextSpan("Cansado de ver as economias escorrerem pelas mãos, nasceu o "),
                            ft.TextSpan("Bolso Furado", ft.TextStyle(weight=ft.FontWeight.BOLD, color=self.COR_PRIMARIA)),
                            ft.TextSpan(": uma plataforma visual e descomplicada criada sob medida para "),
                            ft.TextSpan("transformar o caos em controle", ft.TextStyle(weight=ft.FontWeight.BOLD, color=self.COR_DESTAQUE)),
                            ft.TextSpan(". Em vez de planilhas complexas, o app foi pensado para mostrar com clareza exatamente onde cada centavo é gasto, ajudando você a "),
                            ft.TextSpan("fechar as brechas do seu orçamento!", ft.TextStyle(weight=ft.FontWeight.BOLD, color=self.COR_PRIMARIA)),
                        ],
                        size=15,
                        color=self.COR_TEXTO,
                        text_align=ft.TextAlign.JUSTIFY,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=12,
            ),
            bgcolor=self.COR_CARTAO,
            padding=40,
            border_radius=20,
            border=ft.Border.all(width=1, color=self.COR_BORDA),
            shadow=ft.BoxShadow(
                blur_radius=16,
                color="#0D000000",
                offset=ft.Offset(0, 4)
            ),
            max_width=880,
        )

        # Painel Principal de Conteúdo
        self.conteudo_principal = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(controls=[self.banner_titulo], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Container(height=15),
                    ft.Row(controls=[self.cartao_historia], alignment=ft.MainAxisAlignment.CENTER)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                scroll=ft.ScrollMode.AUTO,
            ),
            padding=ft.Padding(left=20, top=20, right=20, bottom=30),
            expand=True,
        )

        # Adiciona apenas o painel central 
        self.controls = [self.conteudo_principal]