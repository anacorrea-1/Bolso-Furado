import flet as ft
from src.model.usuario import Usuario

# Paleta de Cores "Bolso Furado"
COR_PRIMARIA = "#004D40"   
COR_DESTAQUE = "#F9A826"   
COR_TEXTO = "#263238"      
COR_FUNDO = "#F1F4F8"      
COR_CARTAO = "#FAFBFB"

# Status e Feedbacks do Sistema 
COR_SUCESSO = "#2EA44E"        
COR_SUCESSO_FUNDO = "#E6F4EA"  
COR_ERRO = "#E53935"           
COR_ERRO_FUNDO = "#FCE8E6"     
COR_ALERTA = "#FB8C00"         
COR_ALERTA_FUNDO = "#FFF3E0"   
COR_INFO = "#1E88E5"   

def main(page: ft.Page):

    page.title = "Bolso Furado"
    page.bgcolor = COR_FUNDO
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.maximized = True

    def verificar():
        verificacao = Usuario.verificar(txt_usuario.value, txt_senha.value)
        if verificacao:
            con_base.bgcolor = COR_SUCESSO_FUNDO
            # Adicione um feedback de sucesso para não quebrar o diálogo abaixo
            snack = ft.SnackBar(
                content=ft.Text(value='Login realizado com sucesso!', color=COR_TEXTO),
                bgcolor=COR_SUCESSO_FUNDO
            )
        else:
            con_base.bgcolor = COR_ERRO_FUNDO
            txt_usuario.border_color = COR_ERRO
            txt_senha.border_color = COR_ERRO
            bt_entrar.color = COR_ERRO
            snack = ft.SnackBar(
                content=ft.Text(
                    value='Login inválido.',
                    color=COR_TEXTO,
                    text_align=ft.TextAlign.CENTER,
                    weight=ft.FontWeight.BOLD
                ),
                bgcolor=COR_ERRO_FUNDO,
                duration=1050
            )
            
        page.show_dialog(snack)
        page.update()
            
    def cadastrar():
        pass

    # Campos do formulário
    txt_usuario = ft.TextField(
        label="Usuário / LOGIN",
        width=320,
        border_radius=10,
        border_color=COR_PRIMARIA,
        focused_border_color=COR_DESTAQUE,
        prefix_icon=ft.Icons.PERSON_OUTLINED,
    )

    txt_senha = ft.TextField(
        label="Senha",
        password=True,
        width=320,
        border_radius=10,
        can_reveal_password=True,
        border_color=COR_PRIMARIA,
        focused_border_color=COR_DESTAQUE,
        prefix_icon=ft.Icons.LOCK_OUTLINED,
    )

    logo_app = ft.Image(
        src="src/view/img/logo.png",
        width=180,
        height=140,
    )

    txt_cadastrar = ft.TextField(
        value="Cadastrar-se", 
        text_style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE, decoration_color= COR_DESTAQUE),
        read_only=True, 
        text_align="center",
        border_width=0,
        mouse_cursor=ft.MouseCursor.CLICK, 
        color=COR_DESTAQUE, 
        on_click=cadastrar,
        height=5)

    bt_entrar = ft.FilledButton(content="ENTRAR",bgcolor=COR_DESTAQUE,width=300, on_click=verificar)

    campos = ft.Column(
        controls=[logo_app, txt_usuario, txt_senha,bt_entrar, txt_cadastrar],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
        spacing=15,
    )

    con_base = ft.Container(
        content=campos,
        padding=30,
        alignment=ft.Alignment.CENTER,                     
        bgcolor=COR_CARTAO,
        width=400,
        border_radius=16,
        shadow=ft.BoxShadow(
            blur_radius=20,
            color="#1A000000",
            offset=ft.Offset(0, 5)
        )
    )

    page.add(con_base,)
    page.update()

ft.run(main)