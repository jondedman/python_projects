from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    countdown(5*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_mins = count // 60
    count_secs = count % 60
    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_secs}")
    if count > 0:
        window.after(1000, countdown, count - 1)
    else:
        start_button.config(text="Start", command=start_timer)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


title_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
reset_button = Button(text="Reset", highlightthickness=0)
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
ticks_label = Label(text="✓", fg=GREEN, bg=YELLOW)



title_label.grid(column=1, row=0)
reset_button.grid(column=2, row=2)
start_button.grid(column=0, row=2)
ticks_label.grid(column=1, row=3)

window.mainloop()
