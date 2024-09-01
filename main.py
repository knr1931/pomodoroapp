from tkinter import *
from constants import *
import math

reps = 0
timer = ""


def start_timer():
    global reps
    reps += 1

    long_break_seconds = LONG_BREAK_MIN * MIN_TO_SECONDS_CONVERTOR
    short_break_seconds = SHORT_BREAK_MIN * MIN_TO_SECONDS_CONVERTOR
    work_seconds = WORK_MIN * MIN_TO_SECONDS_CONVERTOR

    if reps % 8 == 0:
        count_down(long_break_seconds)
        timer_heading_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_seconds)
        timer_heading_label.config(text="Break", fg=PINK)
    else:
        count_down(work_seconds)
        timer_heading_label.config(text="Work", fg=GREEN)


def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_heading_label.config(text="Timer")
    check_label.config(text="")
    reps = 0


def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds:02}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_check_marks = ""
        num_work_sessions = math.floor(reps / 2)
        for _ in range(num_work_sessions):
            work_check_marks += CHECK_MARK_TEXT
        check_label.config(text=work_check_marks)


window = Tk()
window.title("Pomodoro App")
window.config(padx=CANVAS_PADDING_X, pady=CANVAS_PADDING_Y, bg=YELLOW)

timer_heading_label = Label(text="Timer", fg=TIMER_TEXT_COLOR,
                            font=TIMER_TEXT_FONT_TYPE, bg=YELLOW, highlightthickness=0)
timer_heading_label.grid(row=0, column=1)

canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=YELLOW, highlightthickness=0)
tomato_background_image = PhotoImage(file=CANVAS_TOMATO_IMAGE_FILE)
canvas.create_image(CANVAS_X_POSITION, CANVAS_Y_POSITION, image=tomato_background_image)
timer_text = canvas.create_text(CANVAS_TEXT_X_POSITION, CANVAS_TEXT_Y_POSITION, text="00:00",
                                fill=CANVAS_TEXT_FILL_COLOR, font=CANVAS_TEXT_FONT_TYPE)
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

check_label = Label(fg=CHECK_MARK_TEXT_COLOR, font=CHECK_MARK_FONT_TYPE, bg=YELLOW, highlightthickness=0)
check_label.grid(row=3, column=1)

window.mainloop()
