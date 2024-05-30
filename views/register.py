from typing import Union
import flet as ft
from views.Router import Router

def Register(router_data: Union[Router, str, None] = None):
    # Crear campos de entrada de texto
    nombre_input = ft.TextField(label="Nombre", autofocus=True)
    edad_input = ft.TextField(label="Edad", keyboard_type="number")

    # Función para manejar el envío del formulario
    def submit_form(e):
        print("hola")
        nombre = nombre_input.value
        edad = edad_input.value

        if int(edad_input.value) != int:
            router_data.page.add(ft.Text(f"Edad Invalida."))

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
            router_data.page.go("/home")
            router_data.page.update()                
            with open ("./views/data.csv","w") as writer:
                writer.write("1,"+str(nombre)+","+str(edad))
            writer.close()

    

    submit_button = ft.ElevatedButton(
        "Enviar",
        on_click=submit_form,
        animate_scale=ft.animation.Animation(500, "bounceOut"), 
    )


    edad_input = ft.TextField(
        label="edad",
        autofocus=True,
        text_style=ft.TextStyle(color="#000000"),
        keyboard_type="text",
    )

    nombre_input = ft.TextField(
        label="Nombre",
        autofocus=True,
        text_style=ft.TextStyle(color="#000000"),
        keyboard_type="text",
    )

    # Contenedores
    div_5 = ft.Container(
        width=259,
        height=70,
        border_radius=21,
        
        alignment=ft.alignment.center,
        content=nombre_input,
    )
    div_7 = ft.Container(
        width=259,
        height=70,
        border_radius=21,
        alignment=ft.alignment.center,
        content=edad_input,
    )

    div_container = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Bienvenido a newTab,\ntu fiel compañero en esta nueva etapa.\n",
                    style=ft.TextThemeStyle.HEADLINE_MEDIUM,
                    
                ),
                ft.Text(
                    "Para empezar, me gustaría saber...",
                    style=ft.TextThemeStyle.HEADLINE_MEDIUM,
                    
                ),
                ft.Text(
                    "\nCómo te llamas?",
                    style=ft.TextThemeStyle.HEADLINE_LARGE,
                    
                ),
                div_5,
                ft.Text(
                    "\nQué edad tienes?",
                    style=ft.TextThemeStyle.HEADLINE_LARGE,
                    
                ),
                div_7,
                submit_button,
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.padding.only(top=46, left=37, right=37, bottom=80),
        alignment=ft.alignment.center,
        
        expand=True,
    )

    
    router_data.page.title = "Registro"


    return div_container