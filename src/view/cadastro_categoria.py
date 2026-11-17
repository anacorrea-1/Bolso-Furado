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

        self.categorias = []
        self.cats()

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

        self.lista_categorias = ft.Column(
            controls=self.categorias,
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
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

    def add_cat(self, e):  
        txt_cat = self.txt_usuario.value.strip()
    
        if len(txt_cat) > 0:
            self.txt_usuario.value = ''
            resultado = Categoria.adicionar(categoria=txt_cat, id_usuario=self.id_u)
            self.cats()

    def cats(self):
        lista = Categoria.recuperar_todos(id_usuario=self.id_u)
        self.categorias.clear()
        
        if len(lista) > 0:
            for i in lista:
                id_cat = i['id_categoria']
                a = i['nome']
                b = ft.Container(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.TextField(value=a, color=self.COR_TEXTO, expand=True),
                            ft.Row( 
                                controls=[
                                    ft.FilledButton(icon=ft.Icons.DELETE,icon_color="white",bgcolor=self.COR_ERRO,on_click=lambda:self.del_cat(id_cat),key=id_cat),
                                ]
                            )
                        ]
                    )
                )
                self.categorias.insert(0, b)
        else:
            self.categorias.append(
                ft.Text('Você não possui nenhuma categoria registrada.', color=self.COR_TEXTO)
            )
    def del_cat(self, cat_id):
        Categoria.excluir(id_categoria=cat_id)
        
        self.cats()
    