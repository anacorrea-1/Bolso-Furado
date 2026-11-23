import flet as ft
from src.database.conexao import Conexao


class DespesasPorCategoriaView(ft.View):
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
        self.route = "/despesasporcategoria"
        self.bgcolor = self.COR_FUNDO
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        page.title = "Bolso Furado - Despesas por categoria"
        page.window.maximized = True

        self.page_ref = page
        self.id_u = None
        self.despesas = []

        # Logo
        self.logo_app = ft.Image(
            src="src/view/img/logo.png",
            width=140,
            height=100,
        )

        # Títulos
        self.titulo = ft.Text(
            "Despesas por categoria",
            size=28,
            weight=ft.FontWeight.BOLD,
            color=self.COR_PRIMARIA,
        )
        self.subtitulo = ft.Text(
            "Selecione uma categoria para visualizar os gastos",
            size=15,
            color=self.COR_TEXTO,
        )

        # Seletor de Categoria
        self.dd_categoria = ft.Dropdown(
            label="Selecione a categoria",
            options=[],
            on_select=self.ao_selecionar_categoria,
            border_radius=10,
            border_color=self.COR_DESTAQUE,
            bgcolor="white",
            focused_border_color=self.COR_PRIMARIA,
            text_size=14,
            width=640,  
        )

        # Resumo do total da categoria selecionada
        self.txt_total = ft.Text(
            "Total na categoria: R$ 0,00",
            size=16,
            weight=ft.FontWeight.BOLD,
            color=self.COR_DESTAQUE,
            visible=False,
        )

        # Lista de despesas
        self.lista = ft.Column(
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
                ft.Divider(color="#ECEFF1", height=20),
                self.dd_categoria,
                ft.Divider(color="#ECEFF1", height=20),
                self.txt_total,
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

        # Inicializa a tela
        self.carregar_dados_iniciais()

    def carregar_dados_iniciais(self):
        usuario = self.page_ref.session.store.get("usuario_logado")
        if not usuario and hasattr(self.page_ref.session, "get"):
            usuario = self.page_ref.session.get("usuario_logado")

        if usuario:
            self.id_u = usuario.get("id_usuario") or usuario.get("id")
            self.carregar_categorias()

        self.lista.controls.append(
            ft.Container(
                content=ft.Text(
                    "Escolha uma categoria acima para listar as despesas.",
                    color="#647078",
                ),
                padding=20,
            )
        )

    def carregar_categorias(self):
        if not self.id_u:
            return

        con, cur = Conexao.conectar()
        if not con:
            return

        try:
            cur.execute(
                "SELECT nome, id_categoria FROM tb_categorias WHERE id_usuario = %s;",
                (self.id_u,),
            )
            categorias = cur.fetchall() or []
            self.dd_categoria.options = [
                ft.dropdown.Option(key=str(c["id_categoria"]), text=c["nome"])
                for c in categorias
            ]
        except Exception as err:
            print(f"Erro ao carregar categorias: {err}")
        finally:
            cur.close()
            con.close()

    def ao_selecionar_categoria(self, e):
        if not self.dd_categoria.value or not self.id_u:
            return

        id_categoria = int(self.dd_categoria.value)
        con, cur = Conexao.conectar()
        if not con:
            return

        try:
            cur.execute(
                """
                SELECT id_despesa, id_categoria, descricao, valor, data_despesa
                FROM tb_despesas
                WHERE id_usuario = %s AND id_categoria = %s
                ORDER BY data_despesa DESC, id_despesa DESC;
                """,
                (self.id_u, id_categoria),
            )
            self.despesas = cur.fetchall() or []
        except Exception as err:
            print(f"Erro ao buscar despesas por categoria: {err}")
            self.despesas = []
        finally:
            cur.close()
            con.close()

        self.atualizar_lista()

    def atualizar_lista(self):
        self.lista.controls.clear()

        if len(self.despesas) > 0:
            total = sum(float(d["valor"]) for d in self.despesas)
            total_fmt = (
                f"R$ {total:,.2f}".replace(",", "X")
                .replace(".", ",")
                .replace("X", ".")
            )
            self.txt_total.value = f"Total na categoria: {total_fmt}"
            self.txt_total.visible = True

            for d in self.despesas:
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
                                        data,
                                        color="#647078",
                                        size=12,
                                    ),
                                ],
                                spacing=5,
                                expand=True,
                            ),
                            ft.Text(
                                f"R$ {valor:,.2f}".replace(",", "X")
                                .replace(".", ",")
                                .replace("X", "."),
                                color=self.COR_ERRO,
                                weight=ft.FontWeight.BOLD,
                            ),
                            ft.IconButton(
                                icon=ft.Icons.DELETE_OUTLINE,
                                icon_color=self.COR_ERRO,
                                on_click=lambda e, id=d["id_despesa"]: self.del_despesa(id),
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
            self.txt_total.visible = False
            self.lista.controls.append(
                ft.Text(
                    "Nenhuma despesa registrada nesta categoria.",
                    color=self.COR_TEXTO,
                )
            )

        self.update()

    def del_despesa(self, id_despesa):
        con, cur = Conexao.conectar()
        if not con:
            return

        try:
            cur.execute(
                "DELETE FROM tb_despesas WHERE id_despesa = %s;",
                (id_despesa,),
            )
            con.commit()
            self.ao_selecionar_categoria(None)
        except Exception as err:
            print(f"Erro ao excluir despesa: {err}")
        finally:
            cur.close()
            con.close()
