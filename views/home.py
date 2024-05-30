from typing import Union
import flet as ft
from views.Router import Router


import csv
from datetime import datetime

def escribir_dato_en_csv(dato):
    
    
    nombre_archivo='datos.csv'

    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    with open(nombre_archivo, mode='a', newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        
        escritor_csv.writerow([dato.control.text, fecha_actual])
        dato.page.update()

def Home_page(router_data: Union[Router, str, None] = None):
    
    container  = ft.Container(
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            expand=True,
            width=480,
            height=800,
            controls=[
                ft.Text("Bienvenido!", style=ft.TextThemeStyle.HEADLINE_LARGE, color="#C9C9C9"),
                ft.Text(
                    "Como te encuentras el dia de hoy del 1 al 5?",
                    style=ft.TextThemeStyle.HEADLINE_LARGE,
                    color="#C9C9C9",
                    
                ),
                ft.Row(
                    wrap=True,
                    spacing=20,
                    run_spacing=20,
                    
                    # width=router_data.page.window_width,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    
                    controls=[
                            ft.Container(
                                content = 
                                    ft.ElevatedButton(
                                    text="1",
                                    on_click= escribir_dato_en_csv,
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=50),
                                        bgcolor="#ADF7B6",
                                        padding=ft.Padding(20, 20, 20, 20),
                                    ),
                                ),
                                     
                                width=100,
                                height=100,
                                border_radius=50,
                            ),
                        ft.Container(
                            content = 
                                ft.ElevatedButton(
                                text="2",
                                on_click= escribir_dato_en_csv,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=50),
                                    bgcolor="#F56767",
                                    padding=ft.Padding(20, 20, 20, 20),
                                ),
                            ),
                            width=100,
                            height=100,
                            bgcolor="#F56767",
                            border_radius=50,
                        ),
                        ft.Container(
                                    content = 
                                        ft.ElevatedButton(
                                        text="3",
                                        on_click= escribir_dato_en_csv,
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=50),
                                            bgcolor="#A0CED9",
                                            padding=ft.Padding(20, 20, 20, 20),
                                        ),
                                    ),
                                    width=100,
                                    height=100,
                                    bgcolor="#A0CED9",
                                    border_radius=50,
                                ),
                                
                                ft.Container(
                                    content = 
                                        ft.ElevatedButton(
                                        text="4",
                                        on_click= escribir_dato_en_csv,
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=50),
                                            bgcolor="#E8DFF5",
                                            padding=ft.Padding(20, 20, 20, 20),
                                        ),
                                    ),
                                    width=100,
                                    height=100,
                                    bgcolor="#E8DFF5",
                                    border_radius=50,
                                ),
                                ft.Container(
                                    content = 
                                        ft.ElevatedButton(
                                        text="5",
                                        on_click= escribir_dato_en_csv,
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=50),
                                            bgcolor="#FCF5C7",
                                            padding=ft.Padding(20, 20, 20, 20),
                                        ),
                                    ),
                                    width=100,
                                    height=100,
                                    bgcolor="#FCF5C7",
                                    border_radius=50,
                                ),
                    ],
                ),
                
                # ft.Row(
                #     alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                #     controls=[
                #         ft.Column(
                #             controls=[
                                

                #             ]
                #         ),
                        
                #     ]
                # ),
                
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        # ft.Text("Tareas", style=ft.TextThemeStyle.HEADLINE_MEDIUM, color="#FFFFFF"),
                        ft.FilledButton(text="TODO", on_click=lambda _: router_data.page.go("/")),
                        ft.FilledButton(text="Clases", on_click=lambda _: router_data.page.go("/Tareas")),
                        ft.FilledButton(text="Inventario", on_click=lambda _: router_data.page.go("/Inventario")),
                        
                        # ft.AppBar(
                        #     leading=ft.Icon(ft.icons.TAG_FACES_ROUNDED),
                        #     leading_width=40,
                        #     title=ft.Text("Flet Router"),
                        #     center_title=False,
                        #     bgcolor=ft.colors.SURFACE_VARIANT,
                        #     actions=[
                        #         ft.IconButton(ft.icons.HOME, on_click=lambda _: router_data.go('/')),
                        #         ft.IconButton(ft.icons.PERSON_ROUNDED, on_click=lambda _: router_data.go('/profile')),
                        #         ft.IconButton(ft.icons.SETTINGS_ROUNDED, on_click=lambda _: router_data.go('/settings'))
                        #     ]
                        # )
                    ],
                ),
            ],
        ),
    )
  
    router_data.page.title = "Home"
    
    return container