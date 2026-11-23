import flet as ft
from src.database.conexao import Conexao


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
        self.id_u = None
        self.despesas = []

        # Logo
        self.logo_app = ft.Image(
            src="src/view/img/logo.png",
            width=140,
            height=100,
        )

        # Título da lista
        self.titulo_lista = ft.Text(
            "Despesas cadastradas",
            size=28,
            weight=ft.FontWeight.BOLD,
            color=self.COR_TEXTO,
        )

        # Resumo do total de gastos
        self.txt_total = ft.Text(
            "Total de gastos: R$ 0,00",
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
                self.titulo_lista,
                ft.Divider(color="#ECEFF1", height=20),
                self.txt_total,
                ft.Divider(color="#ECEFF1", height=20),
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

        # Carrega os dados assim que a tela é montada
        self.carregar_dados(atualizar_tela=False)


    def moeda(self, valor):
        return f"R$ {float(valor):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    def carregar_dados(self, atualizar_tela=True):
        usuario = self.page_ref.session.store.get("usuario_logado")
        if not usuario and hasattr(self.page_ref.session, "get"):
            usuario = self.page_ref.session.get("usuario_logado")

        if usuario:
            self.id_u = usuario.get("id_usuario") or usuario.get("id")

        self.recuperar_despesas()
        self.atualizar_lista(self.despesas, atualizar_tela=atualizar_tela)

    # Recuperar despesas
    def recuperar_despesas(self):
        if not self.id_u:
            self.despesas = []
            return

        con, cur = Conexao.conectar()
        if not con:
            self.despesas = []
            return

        try:
            cur.execute("""
                SELECT id_despesa, id_categoria, descricao, valor, data_despesa
                FROM tb_despesas
                WHERE id_usuario = %s
                ORDER BY data_despesa DESC, id_despesa DESC;
            """, (self.id_u,))
            self.despesas = cur.fetchall() or []
            con.close()
        except Exception as e:
            print(f"Erro ao buscar despesas: {e}")
            self.despesas = []

    # Criar lista de despesas 
    def atualizar_lista(self, despesas=None, atualizar_tela=True):
        if despesas is None:
            despesas = self.despesas

        self.lista.controls.clear()
        self.txt_total.visible = bool(despesas)

        if not despesas:
            self.lista.controls.append(
                ft.Text("Você não possui nenhuma despesa registrada.", color=self.COR_TEXTO)
            )
        else:
            total = sum(float(d["valor"]) for d in despesas)
            self.txt_total.value = f"Total de gastos: {self.moeda(total)}"

            for d in despesas:
                data = (
                    d["data_despesa"].strftime("%d/%m/%Y")
                    if hasattr(d["data_despesa"], "strftime")
                    else str(d["data_despesa"])
                )
                cat = d.get("categoria") or (
                    f"Categoria #{d['id_categoria']}" if d.get("id_categoria") else "Sem categoria"
                )

                self.lista.controls.append(
                    ft.Container(
                        padding=15,
                        bgcolor="white",
                        border_radius=12,
                        border=ft.Border.all(1, "#E5E8EA"),
                        content=ft.Row(
                            controls=[
                                ft.Column(
                                    spacing=5,
                                    expand=True,
                                    controls=[
                                        ft.Text(d["descricao"], color=self.COR_TEXTO, weight=ft.FontWeight.BOLD),
                                        ft.Text(f"{cat} • {data}", color="#647078", size=12),
                                    ],
                                ),
                                ft.Text(self.moeda(d["valor"]), color=self.COR_ERRO, weight=ft.FontWeight.BOLD),
                                ft.IconButton(
                                    icon=ft.Icons.DELETE_OUTLINE,
                                    icon_color=self.COR_ERRO,
                                    on_click=lambda e, id_d=d["id_despesa"]: self.del_despesa(id_d),
                                ),
                            ]
                        ),
                    )
                )

        if atualizar_tela:
            self.update()

    # Excluir despesa
    def del_despesa(self, id_despesa):
        con, cur = Conexao.conectar()
        if not con:
            return

        try:
            cur.execute("DELETE FROM tb_despesas WHERE id_despesa = %s;", (id_despesa,))
            con.commit()
            con.close()
            self.recuperar_despesas()
            self.atualizar_lista(self.despesas)
        except Exception as e:
            print(f"Erro ao excluir despesa: {e}")
