from tkinter import *

BACKGROUND_COLOR = "#33FFCC"
FONT_COLOR = "#330099"

# ------- Background Section --------
window = Tk()
window.title("Habit Pixel")
window.resizable(False, False)
window.geometry("400x450")
window.config(background=BACKGROUND_COLOR)
window.iconbitmap("hobby.ico")

# -------- Introduce Section --------
canvas = Canvas(width=500, height=500, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.place(x=1, y=1)
# --------- Image Section -------------
habit_image = PhotoImage(file='images/image-a.png')
canvas.create_image(200, 250, image=habit_image)

text = Label(
             text="Welcome to the ",
             font=("Monotype Corsiva", 25, "bold"),
             fg=FONT_COLOR,
             background=BACKGROUND_COLOR)
text.place(x=100, y=150)

window.mainloop()
