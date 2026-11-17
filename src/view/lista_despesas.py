
import flet as ft
from src.model.despesas import Despesa


class TodasDespesasView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        # Paleta de Cores "Bolso Furado"
        self.COR_PRIMARIA = "#004D40"
        self.COR_DESTAQUE = "#F9A826"
        self.COR_TEXTO = "#263238"
        self.COR_FUNDO = "#F1F4F8"
        self.COR_CARTAO = "#FAFBFB"

        self.COR_ERRO = "#E53935"
        self.COR_ERRO_FUNDO = "#FCE8E6"

        # Configurações da View
        self.route = "/todasdespesas"
        self.bgcolor = self.COR_FUNDO

        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        page.title = "Bolso Furado - Todas as despesas"
        page.window.maximized = True

        self.page_ref = page

        # Usuário logado
        usuario = page.session.store.get("usuario_logado")
        self.id_u = usuario.get("id_usuario")

        # Recuperar despesas
        self.despesas = []
        self.recuperar_despesas()

        # Logo
        self.logo_app = ft.Image(
            src="src/view/img/logo.png",
            width=140,
            height=100,
        )

        # Título
        self.titulo = ft.Text(
            "Todas as despesas",
            size=28,
            weight=ft.FontWeight.BOLD,
            color=self.COR_PRIMARIA,
        )

        self.subtitulo = ft.Text(
            "Acompanhe e organize seus gastos!",
            size=15,
            color=self.COR_TEXTO,
        )

        # Total gasto
        self.total = ft.Text(
            "",
            size=25,
            weight=ft.FontWeight.BOLD,
            color=self.COR_ERRO,
        )

        self.quantidade = ft.Text(
            "",
            size=13,
            color=self.COR_TEXTO,
        )

        # Cartão de resumo
        self.cartao_total = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        "Total de despesas",
                        color=self.COR_TEXTO,
                    ),
                    self.total,
                    self.quantidade,
                ],
                spacing=5,
            ),
            padding=18,
            bgcolor=self.COR_ERRO_FUNDO,
            border_radius=12,
            width=550,
        )

        # Título da lista
        self.titulo_lista = ft.Text(
            "Despesas cadastradas",
            size=18,
            weight=ft.FontWeight.BOLD,
            color=self.COR_TEXTO,
        )

        # Lista de despesas
        self.lista = ft.Column(
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )

        self.atualizar_total()
        self.atualizar_lista(self.despesas)

        # Organização dos elementos
        self.campos = ft.Column(
            controls=[
                self.logo_app,
                self.titulo,
                self.subtitulo,
                self.cartao_total,
                self.titulo_lista,
                self.lista,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=12,
            expand=True,
        )

        # Cartão principal
        self.con_base = ft.Container(
            content=self.campos,
            padding=30,
            alignment=ft.Alignment.CENTER,
            bgcolor=self.COR_CARTAO,
            width=700,
            height=720,
            border_radius=20,
            shadow=ft.BoxShadow(
                blur_radius=20,
                color="#1A000000",
                offset=ft.Offset(0, 5),
            ),
        )

        self.controls = [self.con_base]

    # Recuperar despesas do banco
    def recuperar_despesas(self):
        self.despesas = Despesa.recuperar_todos(
            id_usuario=self.id_u
        ) or []

    # Atualizar total
    def atualizar_total(self):
        soma = sum(float(d["valor"]) for d in self.despesas)

        self.total.value = (
            f"R$ {soma:,.2f}"
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )

        self.quantidade.value = (
            f"{len(self.despesas)} despesas cadastradas"
        )

    # Criar lista de despesas
    def atualizar_lista(self, despesas):
        self.lista.controls.clear()

        if len(despesas) > 0:

            for d in despesas:

                data = d["data_despesa"]

                if hasattr(data, "strftime"):
                    data = data.strftime("%d/%m/%Y")
                else:
                    data = str(data)

                valor = float(d["valor"])

                linha = ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Column(
                                controls=[
                                    ft.Text(
                                        d["descricao"],
                                        color=self.COR_TEXTO,
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                    ft.Text(
                                        f'{d["categoria"] or "Sem categoria"} • {data}',
                                        color="#647078",
                                        size=12,
                                    ),
                                ],
                                spacing=5,
                                expand=True,
                            ),

                            ft.Text(
                                f"R$ {valor:,.2f}".replace(
                                    ",", "X"
                                ).replace(".", ",").replace("X", "."),
                                color=self.COR_ERRO,
                                weight=ft.FontWeight.BOLD,
                            ),

                            ft.IconButton(
                                icon=ft.Icons.DELETE_OUTLINE,
                                icon_color=self.COR_ERRO,
                                on_click=lambda e, id=d["id_despesa"]:
                                    self.del_despesa(id),
                            ),
                        ],
                    ),
                    padding=15,
                    bgcolor="white",
                    border_radius=12,
                    border=ft.Border.all(1, "#E5E8EA"),
                )

                self.lista.controls.append(linha)

        else:
            self.lista.controls.append(
                ft.Text(
                    "Você não possui nenhuma despesa registrada.",
                    color=self.COR_TEXTO,
                )
            )

    # Pesquisar despesas
    def filtrar_despesas(self, e):
        texto = self.pesquisa.value.lower()

        filtradas = [
            d for d in self.despesas
            if texto in d["descricao"].lower()
            or texto in (d["categoria"] or "").lower()
        ]

        self.atualizar_lista(filtradas)
        self.update()

    # Excluir despesa
    def del_despesa(self, id_despesa):
        resultado = Despesa.excluir(
            id_despesa=id_despesa
        )

        if resultado:
            self.recuperar_despesas()
            self.atualizar_total()
            self.atualizar_lista(self.despesas)
            self.pesquisa.value = ""
            self.update()
