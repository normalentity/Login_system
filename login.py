from flet import *
from time import sleep


def _view_():
    import sqlite3

    # for row in data:
    #     global res
    #     res = row[0]

    # for row1 in data:
    #     global res1
    #     res1 = row1[1]
    def checkcreds(username, password):
        conection = sqlite3.connect("Users.db")
        cursor = conection.cursor()
        query = "SELECT Username,Password FROM Users WHERE Username =? AND Password =?"
        resp = cursor.execute(query, (username, password))
        resp = resp.fetchall()
        if len(resp) > 0:
            return True
        return False

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
            username = page.controls[0].content.controls[0].content.value
            pswd = page.controls[0].content.controls[1].content.value
            if checkcreds(username, pswd):
                print("Logged in successfully")
            else:
                showerror("Invalid username or password")

    page = View(
        route="/login",
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
                    colors.with_opacity(opacity=0.7, color=colors.TEAL_ACCENT_400),
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
                            content=ElevatedButton(
                                text="Login",
                                bgcolor=colors.with_opacity(
                                    opacity=0.2, color=colors.LIGHT_BLUE_600
                                ),
                                icon=icons.LOGIN_OUTLINED,
                                on_click=btn_click,
                            ),
                            margin=margin.only(left=160, top=310),
                            width=150,
                            height=38,
                        ),
                        Container(
                            content=Text(
                                "Forgot Password",
                                italic=True,
                                color=colors.CYAN_700,
                            ),
                            margin=margin.only(left=40, top=440),
                        ),
                        Container(
                            content=Text(
                                "Remember me",
                                italic=True,
                                color=colors.CYAN_700,
                            ),
                            margin=margin.only(left=280, top=440),
                        ),
                        Container(
                            content=Text(
                                "New to the app,",
                                italic=True,
                                spans=[
                                    TextSpan(
                                        text="Register here.",
                                        on_click=lambda e: e.page.go("/sign-up"),
                                    )
                                ],
                                font_family="Helvetica",
                                color=colors.CYAN_700,
                            ),
                            margin=margin.only(left=130, top=50),
                        ),
                    ]
                ),
            )
        ],
    )

    page.bgcolor = colors.with_opacity(opacity=0.3, color=colors.TEAL_ACCENT_200)
    page.padding = padding.only(left=700, top=230)
    return page
