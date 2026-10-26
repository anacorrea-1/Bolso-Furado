import flet as ft

# Paleta de Cores "Bolso Furado"
COR_PRIMARIA = "#004D40"   
COR_DESTAQUE = "#F9A826"   
COR_TEXTO = "#263238"      
COR_FUNDO = "#F1F4F8"      
COR_CARTAO = "#FAFBFB"     

def main(page: ft.Page):

    page.title = "Bolso Furado"
    page.bgcolor = COR_FUNDO
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

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

    campos = ft.Column(
        controls=[logo_app, txt_usuario, txt_senha],
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

    page.add(con_base)
    page.update()

ft.run(main)