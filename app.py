import flet as ft
from flet import *
import flet_fastapi

from pages.login import _view_
from pages.signup import _view1_


def main(page: Page):
    # page.title = "Core"
    page.padding = ft.padding.only(left=700, top=230)
    page.bgcolor = colors.with_opacity(opacity=0.5, color=colors.TEAL_300)

    page.go("/login")
    index = _view_()

    page.views.append(index)

    signu = _view1_()

    def routechange(e: RouteChangeEvent):
        if page.route == "/login":
            page.views.clear()
            page.views.append(index)
        page.update()
        if page.route == "/sign-up":
            page.views.clear()
            page.views.append(signu)
        page.update()

    page.on_route_change = routechange


if __name__ == "__main__":
    app = app(main, port=8000, view=WEB_BROWSER)
