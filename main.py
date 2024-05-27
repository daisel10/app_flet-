import flet as ft
from views.routes import router
from user_controls.app_bar import NavBar
# WIDTH = 800 * 9 / 16
# HEIGHT = 800 * 16 / 9
def main(page: ft.Page):

    page.theme_mode = "dark"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.appbar = NavBar(page)
    
    print("New page size:", page.window_width, page.window_height)
    
    page.on_route_change = router.route_change
    router.page = page
    page.add(
        router.body
    )
    
   
    page.go('/Inventario')
    page.update()

ft.app(target=main, assets_dir="assets")