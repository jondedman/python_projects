from tkinter import *


# 3 different layout managers: pack, place, grid
# pack: simple, but not flexible
# place: absolute positioning
# grid: table-like layout
# padding: add space around the widget or inside the widget
window = Tk()

window.title("My First GUI")
window.minsize(width="500", height="300")
window.config(padx=100, pady=200)

my_label = Label(text="I'm a label", font=("Arial", 24, "bold"))

my_label.grid(row=0, column =0)
my_label["text"] = "new text"
my_label.config(text="hello world")

input = Entry(width=10)
input.grid(row=2, column =3)

def buttonClick():
  my_label["text"] = input.get()

button = Button(text="Click Me", command=buttonClick)
button.grid(row=1, column =1)

new_button =Button(text="New Button")
new_button.grid(row=0, column =2)







window.mainloop()
