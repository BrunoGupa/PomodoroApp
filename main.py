from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
BLUE = "#97BFB4"
SEPIA = "#F5EEDC"
MARRON = "#4F091D"
RED = "#DD4A48"

FONT_NAME = "Courier"
WORK_MIN = 0.01 #25
SHORT_BREAK_MIN = 0.01#5
LONG_BREAK_MIN = 0.01#25

reps = 0
pomodoros = 0


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global pomodoros

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        print("work sec", reps)
        label_time.config(text="WORK", fg=MARRON)
        time_func(work_sec)
    else:
        if reps == 7:
            print("long break", reps)
            label_time.config(text="BREAK", fg=RED)
            time_func(long_break_sec)
        else:
            print("short break", reps)
            label_time.config(text="BREAK", fg=SEPIA)
            time_func(short_break_sec)
    reps += 1
    if reps == 8:
        pomodoros += 1
        checks = "✔" * pomodoros
        label_check.config(text=checks)
        reps = 0
        if pomodoros == 4:
            pomodoros = 0
            label_check.config(text="")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def time_func(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, time_func, count - 1)  # after time in ms, calls a function
    else:
        start_timer()
        print("i am here")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BLUE)  # bg is background

canvas = Canvas(width=200, height=224, bg=BLUE, highlightthickness=0)  # highlightthickness deletes the border
tomato = PhotoImage(file="tomato.png")  # To read my file in tkinter package
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(103, 150, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(row=1, column=1)

# Labels
label_time = Label(text="Timer", fg=SEPIA, font=(FONT_NAME, 40, "bold"), bg=BLUE)  # fg foreground, color of the text
label_time.grid(row=0, column=1)

label_check = Label(fg=RED, font=(FONT_NAME, 20, "bold"), bg=BLUE, highlightthickness=0)
label_check.grid(row=3, column=1)

# Buttons
# start
# calls action() when pressed
button_start = Button(text="Start", command=start_timer, fg=MARRON, font=(FONT_NAME, 13, "bold"), bg=BLUE,
                      highlightthickness=0)
button_start.grid(row=2, column=0)


# reset
def reset():
    print("reset")


# calls action() when pressed
button_reset = Button(text="Reset", command=reset, fg=MARRON, font=(FONT_NAME, 13, "bold"), bg=BLUE,
                      highlightthickness=0)
button_reset.grid(row=2, column=2)





window.mainloop()
