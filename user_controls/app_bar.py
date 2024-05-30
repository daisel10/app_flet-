import flet as ft


def NavBar(page):
    NavBar = ft.AppBar(
            leading_width=40,
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.IconButton(ft.icons.HOME, on_click=lambda _: page.go('/')),
                ft.IconButton(ft.icons.HOME_WORK, on_click=lambda _: page.go('/Tareas')),
                ft.IconButton(ft.icons.INVENTORY, on_click=lambda _: page.go('/Inventario'))
            ]
        )
    
    menubar = ft.MenuBar(
        
        style=ft.MenuStyle(
            alignment=ft.alignment.top_left,
            mouse_cursor={ft.MaterialState.HOVERED: ft.MouseCursor.WAIT,
                          ft.MaterialState.DEFAULT: ft.MouseCursor.ZOOM_OUT},
        ),
        controls=[
            ft.SubmenuButton(
                
                leading=ft.Icon(ft.icons.ADD),
                
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("TODO"),
                        leading=ft.Icon(ft.icons.HOME_WORK),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}),
                        on_click=lambda _: page.go('/')
                      
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Clases"),
                        leading=ft.Icon(ft.icons.CLASS_),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}),
                       on_click=lambda _: page.go('/Tareas')
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Inventario"),
                        leading=ft.Icon(ft.icons.INVENTORY),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}),
                        on_click=lambda _: page.go('/Inventario')
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Emociones"),
                        leading=ft.Icon(ft.icons.EMOJI_EMOTIONS),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}),
                        on_click=lambda _: page.go('/Count_emotions')
                    )
                ]
            ),        
        ]
    )


    return menubar
