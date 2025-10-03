import flet as ft

def aulas_view(page: ft.Page):
    page.title = "Fábrica do Programador"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 500
    page.window.height = 800
    page.window.min_width = 500
    page.window.max_width = 500
    page.window.min_height = 800
    page.window.max_height = 800
    page.window.center()
    page.padding = 0
    # voltar_button = ft.IconButton(
    #         icon="ARROW_BACK",
    #         icon_color="YELLOW",
    #         tooltip="Voltar",
    #         on_click=lambda e: page.go("/home"),

    #     )

    # header = ft.Row(
    #         controls=[voltar_button],
    #         alignment="start"
    #     )

    # ---------- Cores e Tema ----------
    primary_color = ft.Colors.CYAN_400
    card_color = ft.Colors.GREY_800

    # ---------- Função de Navegação ----------
    def navegar(route):
        page.go(route)

    # ---------- Card com ação ----------
    def create_card(title, subtitle, icon, route=None):
        return ft.Card(
            elevation=3,
            color=card_color,
            content=ft.Container(
                content=ft.ListTile(
                    leading=ft.Icon(icon, color=primary_color, size=28),
                    title=ft.Text(title, weight=ft.FontWeight.BOLD, size=16),
                    subtitle=ft.Text(subtitle, size=12, color=ft.Colors.GREY_400),
                    trailing=ft.Icon(ft.Icons.CHEVRON_RIGHT, color=ft.Colors.GREY_500),
                    on_click=lambda e: navegar(route) if route else None,
                ),
                padding=12,
                border_radius=10,
                ink=True,
            ),
            margin=ft.margin.only(bottom=12),
        )

    # ---------- Seções ----------
    def create_section_header(title):
        return ft.Container(
            content=ft.Text(title, size=18, weight=ft.FontWeight.BOLD, color=primary_color),
            margin=ft.margin.only(top=20, bottom=10),
        )

    # ---------- Conteúdo principal ----------
    conteudo = ft.Column(
        [ 
            ft.Icon(ft.Icons.CODE, size=60, color=primary_color),
            ft.Text("Fábrica do Programador",
                    size=24, weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER),
            ft.Text("Desenvolvendo habilidades, construindo o futuro",
                    size=14, color=ft.Colors.GREY_400,
                    text_align=ft.TextAlign.CENTER),

            create_section_header("Módulos de Aprendizado"),
            create_card("Módulo 1: Introdução ao Python",
                        "Fundamentos da linguagem Python", ft.Icons.PLAY_ARROW, "/mod1"),
            create_card("Módulo 2: Estruturas de Controle",
                        "Condicionais e loops", ft.Icons.CODE, "/mod2"),
            create_card("Módulo 3: Projetos Práticos",
                        "Aplicação dos conceitos", ft.Icons.BUILD, "/mod3"),
        ],
        spacing=15,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,  # centraliza verticalmente
    )

    # ---------- Layout ----------
    return ft.View(
        route="/aulas",
        controls=[
            ft.AppBar(
                title=ft.Text("AULAS", size=20, weight=ft.FontWeight.BOLD),
                bgcolor=card_color,
                center_title=True,
                leading=ft.IconButton(ft.Icons.ARROW_BACK,icon_color="white")
            ),
            ft.Container(
                content=conteudo,
                expand=True,
                alignment=ft.alignment.center,  # centraliza dentro do container
                padding=20,
            )
        ],
    )


# ---------- Outras páginas ----------
def modulo_view(page: ft.Page, titulo, descricao):
    return ft.View(
        route=f"/{titulo.lower()}",
        controls=[
            ft.AppBar(
                title=ft.Text(titulo, size=20, weight=ft.FontWeight.BOLD),
                bgcolor=ft.Colors.GREY_800,
                center_title=True,
                leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go("/aulas")),
            ),
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text(descricao, size=16, color=ft.Colors.GREY_300, text_align=ft.TextAlign.CENTER),
                        ft.ElevatedButton("Iniciar", icon=ft.Icons.PLAY_ARROW, on_click=lambda e: print(f"Iniciando {titulo}")),
                    ],
                    spacing=20,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                expand=True,
                alignment=ft.alignment.top_center,
                padding=20,
            ),
        ],
    )


# ---------- Inicialização ----------
def main(page: ft.Page):
    def route_change(e):
        if page.route == "/aulas":
            page.views.clear()
            page.views.append(aulas_view(page))
        elif page.route == "/mod1":
            page.views.append(modulo_view(page, "Módulo 1", "Aprenda os fundamentos do Python."))
        elif page.route == "/mod2":
            page.views.append(modulo_view(page, "Módulo 2", "Entenda condicionais e loops."))
        elif page.route == "/mod3":
            page.views.append(modulo_view(page, "Módulo 3", "Construa projetos práticos."))
        page.update()

    page.on_route_change = route_change
    page.go("/aulas")


ft.app(target=main)
