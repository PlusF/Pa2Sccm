import flet as ft
from view import create_main_view, create_constants_view, create_calculation_view


def main(page: ft.Page):
    page.title = 'Calculator'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 600
    page.window_height = 600

    def nav_bar_clicked(e):
        page_number = int(e.data)
        if page_number == 0:
            page.go('/main')
        elif page_number == 1:
            page.go('/constants')
        elif page_number == 2:
            page.go('/calculation')

    navbar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.CALCULATE_OUTLINED, selected_icon=ft.icons.CALCULATE,
                                     label='Calculator'),
            ft.NavigationDestination(icon=ft.icons.NOTES_OUTLINED, selected_icon=ft.icons.NOTES, label='Constants'),
            ft.NavigationDestination(icon=ft.icons.HELP_OUTLINE_OUTLINED, selected_icon=ft.icons.HELP_OUTLINED,
                                     label='How to Calculate?'),
        ],
        on_change=nav_bar_clicked,
    )

    def route_change(handler):
        troute = ft.TemplateRoute(handler.route)
        page.views.clear()
        if troute.match('/main'):
            page.views.append(create_main_view(page, navbar))
        elif troute.match('/constants'):
            page.views.append(create_constants_view(page, navbar))
        elif troute.match('/calculation'):
            page.views.append(create_calculation_view(page, navbar))
        page.update()

    page.on_route_change = route_change
    page.go('/main')


if __name__ == '__main__':
    ft.app(target=main)
