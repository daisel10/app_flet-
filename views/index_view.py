from typing import Union
import flet as ft
from views.Router import Router
# from State import global_state, State





def IndexView(router_data: Union[Router, str, None] = None):
        
    def add_clicked( e):
        tasks_colunm.controls.append(ft.Checkbox(label=txt_task.value))
        txt_task.value = ""
        view_main_colunm.update()
        print(tasks_colunm.controls)
        
    
    txt_task = ft.TextField(hint_text="Enter task", expand=True)
    tasks_colunm = ft.Column()
    view_main_colunm = ft.Column(
        width=600,
        controls=[
            ft.Row(
                controls=[
                    txt_task,
                    ft.FloatingActionButton(
                        icon=ft.icons.ADD, on_click=add_clicked),
                ],
            ),
            tasks_colunm,
        ],
    )
    
    router_data.page.title = "ToDo App"
    router_data.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    router_data.page.update()
    

    return view_main_colunm
    
    



