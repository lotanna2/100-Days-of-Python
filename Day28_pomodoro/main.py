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
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")

    global reps 
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps # tells python that we are using the global variable 'reps' instead of creating a new local variable and calling it within this function
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

   
    if reps % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text="Break" , fg=RED)
    elif reps % 2 == 0: # Every 2nd rep is a short break
        countdown(short_break_sec)
        title_label.config(text="Short Break" , fg=PINK)
    else: 
        countdown(work_sec)
        title_label.config(text="Work", fg= GREEN)
   
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):

    count_min = math.floor(count / 60) # 'floor' Divides the total seconds by 60 and round down to the nearest whole number
    count_sec = count % 60 # Get the remaining seconds after dividing by 60 and if there's no remainder it will just be '0'
    
    if count_sec < 10:
        count_sec = f"0{count_sec}" # Add a leading zero if the seconds are less than 10

    if count_sec == 0: # If the seconds are exactly 0, set it to "00" for proper display
        count_sec = "00"

    canvas.itemconfig(timer_text, text=f"{count_min} : {count_sec}") # Update the timer text on the image on the tomatoe image on the canvas with the current countdown(count) value
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1) # countdown again after 1 second (1000 milliseconds) with count decreased by 1 minute
    else:
        # When the countdown reaches 0, you can add additional actions here, like starting a break or updating the UI
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2) # Calculate the number of completed work sessions which is 2 reps per work session
        for _ in range(work_sessions):
            marks += "✓"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

count = 5



title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 102, image=tomato_img)
timer_text =canvas.create_text(100, 112, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)






window.mainloop()
