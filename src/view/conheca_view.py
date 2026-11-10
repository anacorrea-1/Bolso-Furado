import flet as ft
from src.model.usuario import Usuario

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

        self.logo_app = ft.Image(
            src="src/view/img/logo.png",
            width=200,
            height=180,
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

        # Banner de bem-vindo 
        self.banner_bem = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text(
                        "Seja Bem-Vindo 'Fulano'!!",
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
            max_width=400,
        )

        # Cartão Principal de História 
        self.cartao_historia = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=self.logo_app,
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
                            ft.TextSpan(". Ele recebia o seu salário, pagava as contas básicas e, quando assustava, o saldo na conta já tinha sumido misteriosamente in pequenas coxinhas no meio da tarde, cafés e gastos imperceptíveis. "),
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

        # Botão de instruções
        self.botao_instrucoes = ft.TextButton(
            "Como usar o aplicativo?",
            on_click=self.abrir_popup,
        )

        self.conteudo_principal = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(height=50), # Espaçador inicial
                    
                    # Coluna para agrupar os títulos um abaixo do outro e centralizados
                    ft.Column(
                        controls=[
                            ft.Row(controls=[self.banner_bem], alignment=ft.MainAxisAlignment.CENTER),
                            ft.Row(controls=[self.banner_titulo], alignment=ft.MainAxisAlignment.CENTER),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    
                    ft.Container(height=15), # Espaço antes de começar o cartão da história
                    ft.Row(controls=[self.cartao_historia], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(controls=[self.botao_instrucoes],alignment=ft.MainAxisAlignment.CENTER,),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                scroll=ft.ScrollMode.AUTO,
            ),
            padding=ft.Padding(left=20, top=20, right=20, bottom=30),
            expand=True,
        )

        # Adiciona apenas o painel central 
        self.controls = [self.conteudo_principal]

    # Função para abrir as instruções
    def abrir_popup(self, e):

        popup = ft.AlertDialog(
            bgcolor="#F5CE90",
            modal=True,
            shape=ft.RoundedRectangleBorder(radius=20),

            title=ft.Text(
                "Como usar o Bolso Furado?",
                size=21,
                weight=ft.FontWeight.BOLD,
                color="#FFFFFF",
                text_align=ft.TextAlign.CENTER,
            ),

            content=ft.Column(
                width=340,
                tight=True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=12,
                controls=[

                    ft.Image(
                        src="src/view/img/mascote.png",
                        width=125,
                        height=115,
                    ),

                    ft.Container(height=5),

                    *[
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Container(
                                        content=ft.Text(
                                            str(i),
                                            color="#004D40",
                                            weight=ft.FontWeight.BOLD,
                                            size=15,
                                        ),
                                        width=30,
                                        height=30,
                                        bgcolor="#F9A826",
                                        border_radius=50,
                                        alignment=ft.Alignment.CENTER,
                                    ),

                                    ft.Text(
                                        texto,
                                        size=14,
                                        color="#263238",
                                        expand=True,
                                    ),
                                ],
                                spacing=12,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            bgcolor="#FAFBFB",
                            padding=12,
                            border_radius=12,
                            width=330,
                        )
                        for i, texto in enumerate([
                            "Cadastre suas receitas e despesas.",
                            "Organize seus gastos por categoria.",
                            "Acompanhe seu dinheiro.",
                            "Controle melhor seu orçamento.",
                        ], start=1)
                    ],
                ],
            ),

            actions=[
                ft.FilledButton(
                    "Entendi!",
                    bgcolor="#F9A826",
                    color="#004D40",
                    on_click=lambda e: self.fechar_popup(popup),
                )
            ],

            actions_alignment=ft.MainAxisAlignment.CENTER,
        )

        self.page.show_dialog(popup)


    # Função para fechar as instruções
    def fechar_popup(self, popup):
        self.page.pop_dialog()
