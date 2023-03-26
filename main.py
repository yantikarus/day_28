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
    global reps
    window.after_cancel(timer)
    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text=f"00:00")
    check_marks.config(text=" ")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break)
        label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="Work", fg=GREEN)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps, timer, mark
    count_minutes = math.floor(count/60)
    count_seconds = count % 60
    if count_seconds ==0:
        count_seconds = "00"
    elif count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        print(reps)
        mark = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            mark +="✔"
        check_marks.config(text=mark)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)



#Label
label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "bold"), bg=YELLOW, highlightthickness=0)
label.grid(row=0, column=1)

#Button
start_btn = Button(text="Start", padx=0, pady=0, bd=0, highlightthickness=0, command=start_timer)
reset_btn = Button(text="Reset", padx=0, pady=0, bd=0, highlightthickness=0, command=reset_timer)
start_btn.grid(row=2, column=0)
reset_btn.grid(row=2, column=2)

#checkmark
check_marks = Label( fg=GREEN, bg=YELLOW)
# text = Text(height=1, width=1)
# text.insert(END, "✔")
check_marks.grid(row=3, column=1)










window.mainloop()
