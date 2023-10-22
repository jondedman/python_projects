from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

button = Button(text="Calculate")
button.grid(column=1,row=3)
input = Entry(width=5)
input.grid(column=1, row=1)
is_equal_to = Label(text="Is equal to")
is_equal_to.grid(column=0, row=2)
km = Label(text="km")
km.grid(column=2, row=2)
km_output = Label(text=0)
km_output.grid(column=1, row=2)
miles = Label(text="Miles")
miles.grid(column=2, row=1)


window.mainloop()
