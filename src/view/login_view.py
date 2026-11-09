import flet as ft
from src.model.usuario import Usuario

class LoginUsuarioView(ft.View):
    def __init__(self, _page: ft.Page):
        super().__init__()

        # Paleta de Cores "Bolso Furado" 
        self.COR_PRIMARIA = "#004D40"   
        self.COR_DESTAQUE = "#F9A826"   
        self.COR_TEXTO = "#263238"      
        self.COR_FUNDO = "#F1F4F8"      
        self.COR_CARTAO = "#FAFBFB"

        # Status e Feedbacks do Sistema 
        self.COR_SUCESSO = "#2EA44E"        
        self.COR_SUCESSO_FUNDO = "#E6F4EA"  
        self.COR_ERRO = "#E53935"           
        self.COR_ERRO_FUNDO = "#FCE8E6"     
        self.COR_ALERTA = "#FB8C00"         
        self.COR_ALERTA_FUNDO = "#FFF3E0"   
        self.COR_INFO = "#1E88E5"   

        # Configurações da View 
        self.route = "/login" 
        self.bgcolor = self.COR_FUNDO
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        _page.title = "Bolso Furado"
        _page.window.maximized = True

        def verificar(e):
            verificacao = Usuario.verificar(self.txt_usuario.value, self.txt_senha.value)
            if verificacao:
                self.con_base.bgcolor = self.COR_SUCESSO_FUNDO
                snack = ft.SnackBar(
                    content=ft.Text(value='Login realizado com sucesso!', color=self.COR_TEXTO),
                    bgcolor=self.COR_SUCESSO_FUNDO
                )
            else:
                self.con_base.bgcolor = self.COR_ERRO_FUNDO
                self.txt_usuario.border_color = self.COR_ERRO
                self.txt_senha.border_color = self.COR_ERRO
                self.bt_entrar.color = self.COR_ERRO
                snack = ft.SnackBar(
                    content=ft.Text(
                        value='Login inválido.',
                        color=self.COR_TEXTO,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD
                    ),
                    bgcolor=self.COR_ERRO_FUNDO,
                    duration=1050
                )
                
            _page.show_dialog(snack)
            _page.update()
            self.page.update()
                
        def cadastrar(e):
            self.page.navigate("/cadastro")

        self.txt_usuario = ft.TextField(
            label="Usuário / LOGIN",
            width=320,
            border_radius=10,
            border_color=self.COR_PRIMARIA,
            focused_border_color=self.COR_DESTAQUE,
            prefix_icon=ft.Icons.PERSON_OUTLINED,
        )

        self.txt_senha = ft.TextField(
            label="Senha",
            password=True,
            width=320,
            border_radius=10,
            can_reveal_password=True,
            border_color=self.COR_PRIMARIA,
            focused_border_color=self.COR_DESTAQUE,
            prefix_icon=ft.Icons.LOCK_OUTLINED,
        )

        self.logo_app = ft.Image(
            src="src/view/img/logo.png",
            width=180,
            height=140,
        )

        
        self.txt_cadastrar = ft.TextButton(
            content=ft.Text("Cadastrar-se"),
            style=ft.ButtonStyle(
                color=self.COR_DESTAQUE,
                overlay_color=ft.Colors.TRANSPARENT,
            ),
            on_click=cadastrar
        )

        self.bt_entrar = ft.FilledButton(
            content=ft.Text("ENTRAR"),
            bgcolor=self.COR_DESTAQUE,
            width=300, 
            on_click=verificar
        )

        self.campos = ft.Column(
            controls=[self.logo_app, self.txt_usuario, self.txt_senha, self.bt_entrar, self.txt_cadastrar],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
            spacing=15,
        )

        self.con_base = ft.Container(
            content=self.campos,
            padding=30,
            alignment=ft.Alignment.CENTER,                     
            bgcolor=self.COR_CARTAO,
            width=400,
            border_radius=16,
            shadow=ft.BoxShadow(
                blur_radius=20,
                color="#1A000000",
                offset=ft.Offset(0, 5)
            )
        )

        self.controls = [self.con_base]
