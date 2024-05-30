from typing import Union
import flet as ft
from views.Router import Router

def Register(router_data: Union[Router, str, None] = None):
    # Crear campos de entrada de texto
    nombre_input = ft.TextField(label="Nombre", autofocus=True)
    edad_input = ft.TextField(label="Edad", keyboard_type="number")

    # Función para manejar el envío del formulario
    def submit_form(e):
        nombre = nombre_input.value
        edad = edad_input.value

        if nombre.strip() == "":
            nombre_input.error_text = "Por favor, ingresa tu nombre"
            router_data.page.update()
        elif edad.strip() == "":
            edad_input.error_text = "Por favor, ingresa tu edad"
            router_data.page.update()
        else:
            nombre_input.error_text = None
            edad_input.error_text = None
            router_data.page.add(ft.Text(f"¡Hola, {nombre}! Tienes {edad} años."))

    # Crear botón para enviar el formulario
    submit_button = ft.ElevatedButton("Enviar", on_click=submit_form)

    # Agregar campos de entrada y botón al contenedor principal
    form_container = ft.Container(
        content=ft.Column([
            nombre_input,
            edad_input,
            submit_button
        ]),
        padding=20,
        alignment=ft.alignment.center,
    )

    container = ft.Container(
        content=form_container,  # Contenedor del formulario
        alignment=ft.alignment.center,
        bgcolor="black",
        expand=True,
    )

    router_data.page.title = "Registro"
    # router_data.page.add(container)

    return container