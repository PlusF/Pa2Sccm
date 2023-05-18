import flet as ft
from utils import calculate_volume_cylinder, calculate_mol_from_PVT, calculate_sccm
from constants import *


def create_main_view(page, navbar):
    width_textfield = 100
    width_unit = 30

    def calculate_and_show(e):
        try:
            time_min = float(textfield_time.value)
            pressure_Pa = float(textfield_pressure.value)
            temperature_celsius = float(textfield_temperature.value)
            diameter_mm = float(textfield_diameter.value)
            length_m = float(textfield_length.value)
            volume_m3 = calculate_volume_cylinder(diameter_mm, length_m)
            n_mol = calculate_mol_from_PVT(pressure_Pa, volume_m3, temperature_celsius)
            value_sccm = calculate_sccm(n_mol, time_min)
            set_sccm(value_sccm)
        except ValueError:
            pass

    def set_sccm(value: float):
        text_sccm.value = f'{value:.03f} sccm'
        page.update()

    def set_quartz(e):
        textfield_diameter.value = diameter_quartz
        textfield_length.value = length_quartz
        page.update()

    def set_mullite(e):
        textfield_diameter.value = diameter_mullite
        textfield_length.value = length_mullite
        page.update()

    def copy_to_clipboard(e):
        value_sccm = text_sccm.value.split()[0]
        page.set_clipboard(value_sccm)
        page.show_snack_bar(ft.SnackBar(ft.Text(f"Copied {value_sccm}"), open=True))

    textfield_time = ft.TextField(value='3', text_align=ft.TextAlign.RIGHT, on_change=calculate_and_show,
                                  width=width_textfield)
    textfield_pressure = ft.TextField(value='10', text_align=ft.TextAlign.RIGHT, on_change=calculate_and_show,
                                      width=width_textfield)
    textfield_temperature = ft.TextField(value='25', text_align=ft.TextAlign.RIGHT, on_change=calculate_and_show,
                                         width=width_textfield)
    button_quartz = ft.ElevatedButton('Quartz', on_click=set_quartz, tooltip='Set the size of the quartz tube')
    button_mullite = ft.ElevatedButton('Mullite', on_click=set_mullite, tooltip='Set the size of the mullite tube')
    textfield_diameter = ft.TextField(value=diameter_quartz, text_align=ft.TextAlign.RIGHT,
                                      on_change=calculate_and_show, width=width_textfield, tooltip='Diameter')
    textfield_length = ft.TextField(value=length_quartz, text_align=ft.TextAlign.RIGHT, on_change=calculate_and_show,
                                    width=width_textfield, tooltip='Length')
    button_copy = ft.IconButton('copy', on_click=copy_to_clipboard, tooltip='Copy')
    text_sccm = ft.Text('???.??? sccm')

    calculate_and_show(None)

    return ft.View('main', [
        ft.Column([
            ft.Row([
                ft.Column([
                    ft.Row(
                        [textfield_time, ft.Text('min', width=width_unit)],
                    ),
                    ft.Row(
                        [textfield_pressure, ft.Text('Pa', width=width_unit)],
                    ),
                    ft.Row(
                        [textfield_temperature, ft.Text('℃', width=width_unit)],
                    ),
                ]),

                ft.Column([
                    ft.Row(
                        [button_quartz, button_mullite],
                    ),
                    ft.Row(
                        [ft.Icon(ft.icons.CIRCLE_OUTLINED, color='indigo', tooltip='Diameter'), textfield_diameter, ft.Text('mm', width=width_unit, tooltip='Diameter')],
                    ),
                    ft.Row(
                        [ft.Icon(ft.icons.ALIGN_HORIZONTAL_RIGHT_OUTLINED, color='indigo', tooltip='Length'), textfield_length, ft.Text('m', width=width_unit, tooltip='Length')],
                    ),
                ]),
            ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),

            ft.Row(
                [button_copy, text_sccm],
                alignment=ft.MainAxisAlignment.CENTER
            ),
        ]),
        navbar
    ], vertical_alignment=ft.MainAxisAlignment.CENTER)


def create_constants_view(page, navbar):
    md = f"""
# Table of Constant Values
    
|**Name**|**Value**      |
|--------|---------------|
|π       |{PI}           |
|0 ℃    |{T_0} K        |
|R       |{R} J/mol K    |
|V_std   |{V_std_m3} m^3 |
    """
    return ft.View('constants', [
        ft.Markdown(
            md,
            selectable=True,
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
            on_tap_link=lambda e: page.launch_url(e.data),
        ),
        navbar
    ], vertical_alignment=ft.MainAxisAlignment.CENTER)


def create_calculation_view(page, navbar):
    md = """
# Calculation
### 1. Calculate volume of the system
V = π d^2 / 4

### 2. Calculate n [mol] from pressure, volume, and temperature
n = pV / RT

### 3. Calculate the standard volume of n [mol] gas and divide by time
sccm = V_std n / t

### Notes: Be careful for the units.

    """
    return ft.View('constants', [
        ft.Markdown(
            md,
            selectable=True,
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
            on_tap_link=lambda e: page.launch_url(e.data),
        ),
        navbar
    ], vertical_alignment=ft.MainAxisAlignment.CENTER)
