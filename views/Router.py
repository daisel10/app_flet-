from typing import Callable, Any
import flet as ft

from user_controls.app_bar import NavBar



class Router:
    def __init__(self):
        self.data = dict()
        self.routes = {}
        self.body = ft.Container(
            alignment=ft.alignment.center,
            expand=True
            #bgcolor="yellow"
            )

    def set_route(self, stub: str, view: Callable):
        self.routes[stub] = view
    
    def set_routes(self, route_dictionary: dict):
        """Sets multiple routes at once. Ex: {"/": IndexView }"""
        self.routes.update(route_dictionary)

    def route_change(self, route):
        _page = route.route.split("?")[0]
        
        print(_page)
        if (_page != "/screen_lock") and (_page != "/register") :
            route.page.appbar = NavBar(route.page)
        

        self.body.content = self.routes[_page](self)
        self.body.update()

