from tkinter import *
import time

# ------ Constant
BACKGROUND_COLOR = "#33FFCC"
FONT_COLOR = "#330099"
INTRODUCE_TEXT = "Are you looking to build positive habits and track your progress over time? Look no further than'\n' " \
                 "HabitApp! Our innovative application is designed to help you develop and maintain healthy habits,'\n' " \
                 "with the added feature of integrating with Pixela graph for visualizing your progress."
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
canvas.place(x=1, y=1)
# --------- Image Section -------------
canvas.create_image(200, 250, image=habit_image)
text = Label(
    text="Welcome to '\n' a Powerful Tool '\n' to Track and Improve Your",
    font=("Monotype Corsiva", 25, "bold"),
    fg=FONT_COLOR,
    background=BACKGROUND_COLOR)

text.place(x=10, y=80)


def clean_page():
    canvas.destroy()
    text.destroy()


window.after(5000, clean_page)


def intro_text():
    inro_text = Label(text=INTRODUCE_TEXT,
                      font=("Monotype Corsiva", 14, "bold"),
                      fg=FONT_COLOR,
                      background=BACKGROUND_COLOR)
    inro_text.place(x=10, y=10)


window.after(6000, intro_text)
window.mainloop()
