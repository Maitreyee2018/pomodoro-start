from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)                      #stop the timer
    canvas.itemconfig(timer_text, text="00:00")     #show 00.00 in the timer area
    label.config(text="Timer")                      #show the original label
    tick_label.config(text="")                      #wipe out the check marks

    global reps
    reps = 0                                        #setting the reps to 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1                                      #increment reps

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)
    elif reps == 2 or reps == 4 or reps == 6:
        label.config(text="Mini Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    elif reps == 8:
        label.config(text="Big Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)              #to show the minute value
    count_sec = count % 60                          #to show the secs value
    # python dynamic typing/assignment
    if count_sec < 10:
        count_sec = "0" + str(count_sec)            #format for time < 10 secs

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")   #show timer

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)           #set the timer
    else:
        start_timer()                                               #call back start timer
        check_mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            check_mark += "✓"

        tick_label.config(text=check_mark)                         #populate check marks


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button()
start_button.config(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button()
reset_button.config(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

tick_label = Label()
tick_label.config(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
tick_label.grid(column=1, row=3)

window.mainloop()
