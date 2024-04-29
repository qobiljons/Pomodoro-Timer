from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_all():
    window.after_cancel(timer)
    lbl_timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(canvas_text, text=f"00:00")
    lbl_tick.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        lbl_timer.config(text="Long Break", fg=PINK)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        lbl_timer.config(text="Break", fg=RED)
    else:
        lbl_timer.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)
    reps += 1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    minute = math.floor(count/60)
    if minute < 10:
        minute = f"0{minute}"
    second = count % 60
    if second < 10:
        second = f"0{second}"
    canvas.itemconfig(canvas_text, text=f"{minute}:{second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        work_num = math.floor(reps/2)
        marks = ""
        for i in range(work_num):
            marks += "✓"
            lbl_tick.config(text=marks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(bg=YELLOW, padx=100, pady=50)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
canvas_text = canvas.create_text(100, 130, font=(FONT_NAME, 35, "bold"), text="00:00", fill="white")
canvas.grid(column=1, row=1)
# Label

lbl_timer = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
lbl_timer.grid(column=1, row=0, columnspan=2)
# Button

btn_start = Button(text="Start", command=start_timer)
btn_start.grid(column=0, row=2)
btn_reset = Button(text="Reset", command=reset_all)
btn_reset.grid(column=2, row=2)

lbl_tick = Label(text="", font=(FONT_NAME, 45, "bold"), bg=YELLOW, fg=GREEN)
lbl_tick.grid(column=1, row=3)


window.mainloop()
