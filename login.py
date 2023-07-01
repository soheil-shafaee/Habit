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


def intr_text():
    inro_text = Label(text=INTRODUCE_TEXT,
                      font=("Monotype Corsiva", 14, "bold"),
                      fg=FONT_COLOR,
                      background=BACKGROUND_COLOR)

    def cleaning():
        btn_go.destroy()
        inro_text.destroy()

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

# -------- Cleaning Page -----------


window.mainloop()
