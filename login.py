from tkinter import *
import time

# ------ Constant
BACKGROUND_COLOR = "#33FFCC"
FONT_COLOR = "#330099"
INTRODUCE_TEXT = "Are you looking to build positive \n habits and track \n your progress over time? Look no further " \
                 "than\n " \
                 "HabitApp!\n Our innovative application is designed to \n help you develop and maintain healthy " \
                 "habits," \
                 "\n " \
                 "with the added feature of integrating with \n Pixela graph for visualizing your progress."
# ------- Background Section --------
window = Tk()
window.title("Habit Pixel")
window.resizable(False, False)
window.geometry("400x450")
window.config(background=BACKGROUND_COLOR)
window.iconbitmap("hobby.ico")

# -------- Welcome Section --------
habit_image = PhotoImage(file='images/image-a.png')
canvas = Canvas(width=500, height=500, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.place(x=5, y=5)
# --------- Image Section -------------
canvas.create_image(200, 300, image=habit_image)
text = Label(
    text="Welcome to \n a Powerful Tool \n to Track and Improve Your",
    font=("Monotype Corsiva", 25, "bold"),
    fg=FONT_COLOR,
    background=BACKGROUND_COLOR)

text.place(x=10, y=80)


# -------- Cleaning Page -----------
def clean_page():
    text.destroy()
    canvas.destroy()


window.after(1000, clean_page)


# ------- Introduce Text --------
def intr_text():
    inro_text = Label(text=INTRODUCE_TEXT,
                      font=("Monotype Corsiva", 14, "bold"),
                      fg=FONT_COLOR,
                      background=BACKGROUND_COLOR)

    # -------- Cleaning Page -----------
    def cleaning():
        btn_go.destroy()
        inro_text.destroy()
        signin()

    btn_go = Button(
        text="Let's Go",
        width=10,
        background=FONT_COLOR,
        fg=BACKGROUND_COLOR,
        command=cleaning
    )
    inro_text.place(x=10, y=120)
    btn_go.place(x=150, y=320)


window.after(2000, intr_text)


# --------- Signin Section ---------
def signin():
    sign_in = Label(text="Sign in",
                    font=("Monotype Corsiva", 20, "bold"),
                    fg=FONT_COLOR,
                    background=BACKGROUND_COLOR)
    sign_in.place(x=10, y=10)

    user_name_label = Label(text='User Name:',
                            font=("Monotype Corsiva", 15, "bold"),
                            fg=FONT_COLOR,
                            background=BACKGROUND_COLOR)
    user_name_entry = Entry(width=35)
    user_name_label.place(x=20, y=20)
    user_name_entry.place(x=182, y=20)

    password_label = Label(text='Password:',
                           font=("Monotype Corsiva", 15, "bold"),
                           fg=FONT_COLOR,
                           background=BACKGROUND_COLOR)
    password_entry = Entry(width=35)
    password_label.place(x=20, y=250)
    password_entry.place(x=182, y=250)

    graph_id_label = Label(text='Graph ID:',
                           font=("Monotype Corsiva", 15, "bold"),
                           fg=FONT_COLOR,
                           background=BACKGROUND_COLOR)
    graph_id_entry = Entry(width=35)
    graph_id_label.place(x=20)
    graph_id_entry.place(x=182, y=)

    email_label = Label(text='Email:',
                        font=("Monotype Corsiva", 15, "bold"),
                        fg=FONT_COLOR,
                        background=BACKGROUND_COLOR)
    email_entry = Entry(width=35)
    email_label.place(x=20, y=150)
    email_entry.place(x=182, y=200)

    email_password_label = Label(text='Email Password:',
                                 font=("Mono-type Corsiva", 15, "bold"),
                                 fg=FONT_COLOR,
                                 background=BACKGROUND_COLOR)
    email_password_entry = Entry()
    email_password_label.place(x=20, y=250)
    email_password_entry.place(x=182, y=255)


window.mainloop()
