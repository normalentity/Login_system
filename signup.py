from flet import *
from time import sleep
from saveuser import save_user


def _view1_():
    def showerror(msg, type="username"):
        if type == "username":
            control = 0
        elif type == "password":
            control = 1
        page.controls[0].content.controls[control].content.error_text = msg
        page.update()
        sleep(2)
        page.controls[0].content.controls[control].content.error_text = None
        page.update()

    def btn_click(e):
        if not page.controls[0].content.controls[0].content.value:
            showerror("Username cannot be empty")
        elif len(page.controls[0].content.controls[0].content.value) > 8:
            showerror("Username cannot be longer than 8 characters")
        if not page.controls[0].content.controls[1].content.value:
            showerror("Password cannot be empty", type="password")
        elif len(page.controls[0].content.controls[1].content.value) > 8:
            showerror("Password cannot be longer than 8 characters", type="password")
        else:
            save_user(
                Records=(
                    page.controls[0].content.controls[0].content.value,
                    page.controls[0].content.controls[1].content.value,
                )
            )

    page = View(
        route="/sign-up",
        controls=[
            Container(
                height=500,
                width=450,
                bgcolor=colors.with_opacity(opacity=0.1, color=colors.WHITE10),
                border_radius=border_radius.all(20),
                blur=Blur(200, 200, BlurTileMode.MIRROR),
                shadow=BoxShadow(
                    200,
                    200,
                    colors.with_opacity(opacity=0.4, color=colors.TEAL_ACCENT_400),
                    Offset(55, 200),
                    ShadowBlurStyle.INNER,
                ),
                content=Stack(
                    controls=[
                        Container(
                            content=TextField(
                                label="Username",
                                border="underline",
                                hint_text="Enter your username",
                                bgcolor=colors.with_opacity(
                                    opacity=0.3, color=colors.BLACK26
                                ),
                                filled=True,
                            ),
                            margin=margin.only(left=80, top=150),
                            width=300,
                            height=70,
                        ),
                        Container(
                            width=300,
                            height=70,
                            content=TextField(
                                label="Password",
                                border="underline",
                                hint_text="Enter your password",
                                bgcolor=colors.with_opacity(
                                    opacity=0.3, color=colors.BLACK26
                                ),
                                filled=True,
                                password=True,
                                can_reveal_password=True,
                            ),
                            margin=margin.only(left=80, top=230),
                        ),
                        Container(
                            content=Text(
                                "Resgistered? ,",
                                style=FontWeight(value="w400"),
                                italic=True,
                                spans=[
                                    TextSpan(
                                        text="Login here.",
                                        on_click=lambda e: e.page.go("/login"),
                                    )
                                ],
                                font_family="Helvetica",
                            ),
                            margin=margin.only(left=130, top=50),
                        ),
                        Container(
                            content=ElevatedButton(
                                text="Sign Up",
                                bgcolor=colors.with_opacity(
                                    opacity=0.2, color=colors.LIGHT_BLUE_600
                                ),
                                icon=icons.DRAW,
                                on_click=btn_click,
                            ),
                            margin=margin.only(left=160, top=310),
                            width=150,
                            height=38,
                        ),
                    ]
                ),
            )
        ],
    )

    page.bgcolor = colors.with_opacity(opacity=0.4, color=colors.LIGHT_BLUE_700)
    # page.bgcolor = "21211f"
    page.padding = padding.only(left=700, top=230)
    # "#c28e00"
    return page
