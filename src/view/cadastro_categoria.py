from src.model.categoria import Categoria
import flet as ft

class CadastroCategoriaoView(ft.View):
    def __init__(self, _page: ft.Page):
        super().__init__()

        # Paleta de Cores "Bolso Furado"
        self.COR_PRIMARIA = "#004D40"
        self.COR_DESTAQUE = "#F9A826"
        self.COR_TEXTO = "#263238"
        self.COR_FUNDO = "#F1F4F8"
        self.COR_CARTAO = "#FAFBFB"

        # Cores de feedback
        self.COR_SUCESSO = "#2EA44E"
        self.COR_ERRO = "#E53935"

        # Configurações da View
        self.route = "/cadcate"
        self.bgcolor = self.COR_FUNDO
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        _page.title = "Bolso Furado - Cadastro de categoria"
        _page.window.maximized = True

        id_usuario = _page.session.store.get("usuario_logado")
        self.id_u = id_usuario.get("id_usuario")

        # Logo
        self.logo_app = ft.Image(
            src="src/view/img/mascote.png",
            width=160,
            height=110,
        )

        # Título
        self.titulo = ft.Text(
            "Minhas categorias",
            size=28,
            weight=ft.FontWeight.BOLD,
            color=self.COR_PRIMARIA,
        )

        self.subtitulo = ft.Text(
            "Organize seus gastos de maneira simples!",
            size=15,
            color=self.COR_TEXTO,
        )

        # Campo de cadastro
        self.txt_usuario = ft.TextField(
            hint_text="Digite uma categoria",
            expand=True,
            height=48,
            border_radius=10,
            border_color=self.COR_PRIMARIA,
            focused_border_color=self.COR_DESTAQUE,
            prefix_icon=ft.Icons.ADD,
            on_submit=self.add_cat
        )

        # Botão adicionar
        self.bt_entrar = ft.FilledIconButton(
            icon=ft.Icons.ADD,
            icon_color="white",
            bgcolor=self.COR_DESTAQUE,
            width=55,
            height=48,
            on_click=self.add_cat
        )

        # Campo e botão lado a lado
        self.linha_cadastro = ft.Row(
            controls=[
                self.txt_usuario,
                self.bt_entrar,
            ],
            spacing=10,
        )

        # Título da lista
        self.titulo_lista = ft.Text(
            "Categorias cadastradas",
            size=18,
            weight=ft.FontWeight.BOLD,
            color=self.COR_TEXTO,
        )

        # Lista de categorias
        self.lista_categorias = ft.Column(
            controls=[
                ft.Text(
                    "Suas categorias aparecerão aqui.",
                    color="#888888",
                    size=14,
                )
            ],
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
        )

        # Organização dos elementos
        self.campos = ft.Column(
            controls=[
                self.logo_app,
                self.titulo,
                self.subtitulo,
                self.linha_cadastro,
                ft.Divider(color="#E5E8EA"),
                self.titulo_lista,
                self.lista_categorias,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
            expand=True,
        )

        # Cartão principal
        self.con_base = ft.Container(
            content=self.campos,
            padding=35,
            alignment=ft.Alignment.CENTER,
            bgcolor=self.COR_CARTAO,
            width=650,
            height=680,
            border_radius=20,
            shadow=ft.BoxShadow(
                blur_radius=20,
                color="#1A000000",
                offset=ft.Offset(0, 5),
            ),
        )

        self.controls = [self.con_base]

    def add_cat(self):
        txt_cat = self.txt_usuario.value
        if len(txt_cat)> 0:
            self.txt_usuario.value = ''
            Categoria.adicionar(txt_cat,self.id_u)
        else:
            pass

