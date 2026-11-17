import flet as ft
import datetime

from src.model.categoria import Categoria
from src.model.despesas import Despesa

class CadastroDespesaView(ft.View):

    def __init__(self, page: ft.Page):
        super().__init__()

        # Paleta de cores Bolso Furado
        self.COR_PRIMARIA = "#004D40"
        self.COR_DESTAQUE = "#F9A826"
        self.COR_TEXTO = "#263238"
        self.COR_FUNDO = "#F1F4F8"
        self.COR_CARTAO = "#FAFBFB"

        self.COR_SUCESSO = "#2EA44E"        
        self.COR_SUCESSO_FUNDO = "#E6F4EA"  
        self.COR_ERRO = "#E53935"           
        self.COR_ERRO_FUNDO = "#FCE8E6"

        # Configurações da View
        self.route = "/caddesp"
        self.bgcolor = self.COR_FUNDO

        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        page.title = "Bolso Furado - Cadastro de despesa"
        page.window.maximized = True

        self.page_ref = page

        # Usuário logado
        usuario = page.session.store.get("usuario_logado")
        self.id_u = usuario.get("id_usuario")

        # Categorias do usuário
        self.lista_categorias = Categoria.recuperar_todos(
            id_usuario=self.id_u
        )

        # Logo
        self.logo_app = ft.Image(
            src="src/view/img/logo.png",
            width=150,
            height=100,
        )

        # Título
        self.titulo = ft.Text(
            "Adicionar despesa",
            size=24,
            weight=ft.FontWeight.BOLD,
            color=self.COR_PRIMARIA,
        )

        self.subtitulo = ft.Text(
            "Preencha as informações abaixo:",
            size=14,
            color=self.COR_TEXTO,
        )

        # Campo descrição
        self.txt_descricao = ft.TextField(
            label="Descrição",
            height=48,
            border_radius=10,
            border_color=self.COR_PRIMARIA,
            focused_border_color=self.COR_DESTAQUE,
            expand=True,
        )

        # Campo valor
        self.txt_valor = ft.TextField(
            label="Valor",
            keyboard_type=ft.KeyboardType.NUMBER,
            width=275,
            border_radius=10,
            border_color=self.COR_PRIMARIA,
            focused_border_color=self.COR_DESTAQUE,
            expand=True,
        )

        #Campo das categorias
        self.dd_categoria = ft.Dropdown(
            label="Categoria",
            hint_text="Selecione a categoria",
            expand=True,
            height=48,
            border_radius=10,
            border_color=self.COR_DESTAQUE,
            options=[
                ft.dropdown.Option(
                    key=str(cat["id_categoria"]),
                    text=cat["nome"],
                )
                for cat in self.lista_categorias
            ],
        )

        #Campo de data
        self.data_selecionada = datetime.date.today()

        def ao_mudar_data(e):
            if self.date_picker.value:
                self.data_selecionada = self.date_picker.value.date()
                self.txt_data.value = self.data_selecionada.strftime("%d/%m/%Y")
                self.txt_data.update()

        self.date_picker = ft.DatePicker(
            first_date=datetime.datetime(2020, 1, 1),
            last_date=datetime.datetime(2035, 12, 31),
            value=datetime.datetime.now(),
            on_change=ao_mudar_data,
        )

        if self.date_picker not in page.overlay:
            page.overlay.append(self.date_picker)

        self.txt_data = ft.TextField(
            label="Data da despesa",
            value=self.data_selecionada.strftime("%d/%m/%Y"),
            read_only=True,
            color=self.COR_TEXTO,
            width=275,
            border_radius=10,
            focused_border_color=self.COR_DESTAQUE,
            suffix_icon=ft.IconButton(
                icon=ft.Icons.CALENDAR_MONTH,
                icon_color=self.COR_PRIMARIA,
                on_click=lambda: page.show_dialog(self.date_picker),
            ),
        )

        # Botão salvar
        self.bt_salvar = ft.FilledButton(
            content="SALVAR DESPESA",
            width=300,
            height=45,
            bgcolor=self.COR_DESTAQUE,
            color="white",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=20)
            ),
            on_click=self.add_despesa
        )

        # Organização dos elementos
        self.linha_elementos = ft.Row(controls=[self.txt_data,self.txt_valor])


        # Cartão principal
        self.con_base = ft.Container(
            content=ft.Column(
                controls=[
                    self.logo_app,
                    self.titulo,
                    self.subtitulo,
                    self.txt_descricao,
                    self.linha_elementos,
                    self.dd_categoria,
                    ft.Divider(color="#ECEFF1", height=20), 
                    self.bt_salvar,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),  
            padding=25,
            bgcolor=self.COR_CARTAO,
            width=600,
            border_radius=20,
            shadow=ft.BoxShadow(
                blur_radius=20,
                color="#1A000000",
                offset=ft.Offset(0, 5),
            ),
        )

        self.controls = [self.con_base]


    def add_despesa(self):
        descricao = self.txt_descricao.value
        valor = self.txt_valor.value
        if valor and valor.find(','):
            valor = valor.replace(',',".")
            try:
                valor = float(valor)
            except:
                valor = None
        data = self.txt_data.value
        dia, mes, ano = data.split('/')
        data = ano + "-" + mes + "-" + dia
        id_cat = self.dd_categoria.value
        if descricao and valor and data and id_cat:
            if Despesa.incluir(id_usuario=self.id_u, descricao=descricao, valor=valor, data_despesa=data, id_categoria=id_cat):
               snack = ft.SnackBar(content=ft.Text(value='Despesa Adicionada!',
                                                    color=self.COR_SUCESSO,
                                                    text_align= ft.TextAlign.CENTER,
                                                    weight=ft.FontWeight.BOLD),
                                    bgcolor=self.COR_SUCESSO_FUNDO,
                                    
                                    duration=1050,
                                    )
            else:
                snack = ft.SnackBar(content=ft.Text(value='Houve um erro, tente novamente.',
                                                    color=self.COR_ERRO,
                                                    text_align= ft.TextAlign.CENTER,
                                                    weight=ft.FontWeight.BOLD),
                                    bgcolor=self.COR_ERRO_FUNDO,
                                    duration=1050,
                                    )
        else:
            snack = ft.SnackBar(content=ft.Text(value='Preencha todos os campos e selecione uma categoria.',
                                                color=self.COR_ERRO,
                                                text_align= ft.TextAlign.CENTER,
                                                weight=ft.FontWeight.BOLD),
                                bgcolor=self.COR_ERRO_FUNDO,
                                duration=1050,
                                )
                
        self.page_ref.show_dialog(snack)

