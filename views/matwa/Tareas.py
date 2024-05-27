from typing import Union
import flet as ft
from views.Router import Router
from views.matwa import funcs
import datetime

WIDTH = 800 * 9 / 16
HEIGHT = 800 * 16 / 9


def Tareas(router_data: Union[Router, str, None] = None):

    page = router_data.page

    container = ft.Container()

    currentClass = funcs.GetCurrentClass()

    try:
        Nombre = currentClass["Nombre"]
        HoraInicio = currentClass["HoraInicio"]
        HoraFin = currentClass["HoraFin"]
        Salon = currentClass["Salon"]
    except:
        Nombre = "No hay clase"
        HoraInicio = ""
        HoraFin = ""
        Salon = ""

    tareas = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(value=f"Nombre : {Nombre}"),
                    ft.Text(value=f"Hora: {HoraInicio} -> {HoraFin}"),
                    ft.Text(value=f"Salon: {Salon}"),
                ],
                width=WIDTH,
            ),
            width=WIDTH,
            padding=10,
        ),
        width=WIDTH,
    )

    taskNameInput = ft.TextField(label="Nombre de la tarea")

    taskDate = None

    def changeDate(e):
        global taskDate
        taskDate = taskDatePicker.value

    taskDatePicker = ft.DatePicker(on_change=changeDate)
    

    def openDatePicker(e):

        taskDatePicker.pick_date()

    def makeTask(e):
        global taskDate
        t = funcs.Task(taskNameInput.value, "", taskDate.date())
        update_tareas()
        page.update()

    tareasP = ft.Column(
        controls=[ft.Text(value=f"{op}") for op in funcs.tasks],
        width=WIDTH,
        scroll=ft.ScrollMode.ALWAYS,
    )

    TareasPendientes = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[ft.Text("Tareas Pendientes:"), tareasP],
                width=WIDTH,
                height=HEIGHT / 4,
                scroll=ft.ScrollMode.ALWAYS,
            ),
            padding=10,
            width=WIDTH,
        )
    )

    def update_tareas():
        tareasP.controls = [ft.Text(value=f"{op}") for op in funcs.tasks]

    pendientes = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(value="Tareas Pendientes:"),
                    taskNameInput,
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(text="Agregar Tarea", on_click=makeTask),
                            ft.ElevatedButton(
                                text="Seleccionar Fecha", on_click=openDatePicker
                            ),
                        ]
                    ),
                ],
                width=WIDTH,
            ),
            width=WIDTH,
            padding=10,
        ),
        width=WIDTH,
    )

    container.content = ft.Column(
        controls=[
            tareas,
            pendientes,
            taskDatePicker,
            TareasPendientes,
        ],
    )

    router_data.page.title = "Tareas"
    router_data.page.add(container)

    return container
