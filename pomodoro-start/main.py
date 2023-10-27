from tkinter import *
import os

# ---------------------------- FILE PATH ------------------------------- #
# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the relative path to the image file
rel_path = "tomato.png"

# Construct the absolute file path
abs_file_path = os.path.join(script_dir, rel_path)

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET
# ------------------------------- #

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    ticks_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break", fg=RED)
    elif reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        title_label.config(text="Break", fg=PINK)
    else:
        countdown(WORK_MIN * 60)
        title_label.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_mins = count // 60
    count_secs = count % 60
    if count_secs < 10:
        count_secs = f"0{count_secs}"
    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_secs}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(reps//2):
            marks += "✓"
        ticks_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=abs_file_path)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


title_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
reset_button = Button(text="Reset", highlightthickness=0, command=reset)
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
ticks_label = Label(fg=GREEN, bg=YELLOW)



title_label.grid(column=1, row=0)
reset_button.grid(column=2, row=2)
start_button.grid(column=0, row=2)
ticks_label.grid(column=1, row=3)

window.mainloop()
