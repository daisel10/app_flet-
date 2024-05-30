from typing import Union
import flet as ft
from views.Router import Router
# from State import global_state, State
import csv

def calcular_promedio_primera_columna(nombre_archivo):
    # Lista para almacenar los valores de la primera columna
    valores = []
    try:
        # Leer el archivo CSV
        with open(nombre_archivo, mode='r') as archivo:
            lector_csv = csv.reader(archivo)
            
            # Iterar sobre cada fila en el CSV
            for fila in lector_csv:
                # Convertir el valor de la primera columna a entero y añadirlo a la lista
                valores.append(int(fila[0]))

        
        promedio = sum(valores) / len(valores) if valores else 0
        
        return promedio
        
    except FileNotFoundError:
        return "Archivo de datos no encontrado"
    

# Usar la función para calcular el promedio de los valores en el archivo 'datos.csv'


def Count_emotions(router_data: Union[Router, str, None] = None):
    router_data.page.title = "Emotions"
    promedio = calcular_promedio_primera_columna('datos.csv')

    pb = ft.ProgressBar(width=400,color="amber")
    pb.value = promedio*2/10
                 
    progresiveBAr= ft.Column(
            controls=[
                ft.Text("Este es el promedio de tu emociones...", style="headlineSmall"),
                ft.Column([ ft.Text(f"Has estado en un {int(promedio)}"), pb]),
            ])
    
    lineas_emergencias = ft.Column(
            [
                ft.Text(
                    "La Línea 106 es atendida las 24 horas los 365 días del año por profesionales de psicología.",
                    style=ft.TextThemeStyle.HEADLINE_SMALL,
                    
                ),
                ft.Text(
                    "la Línea 192 – opción 4",
                    style=ft.TextThemeStyle.HEADLINE_SMALL,
                    
                ),
                ft.Text(
                    "la línea 311 766 8666 para recibir apoyo psicosocial gratuito",
                    style=ft.TextThemeStyle.HEADLINE_SMALL,
                    
                ),
            ]
        )
    felicitaciones = ft.Column(
            [
                ft.Text(
                    "Felicitaciones tus emociones se han mantenido muy bien.",
                    style=ft.TextThemeStyle.HEADLINE_SMALL
                    
                ),
               
            ]
        )
    
    div_container = ft.Container(
        content=ft.Column(
            [
                progresiveBAr,
                lineas_emergencias if promedio < 3 else felicitaciones
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            expand=True,
            width=480,
            height=800,
        )
        
    )
    

    return div_container
    
    



