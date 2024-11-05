from tkinter import *
import math
from numpy.ma.extras import row_stack

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 10
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 7
CHECK_SYMBOL="✔"
REPS=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- #
def time_reset():
    global REPS
    window.after_cancel(timer)
    title.config(text="Timer",fg=fg)
    canvas.itemconfig(timer_text, text=WORK_MIN)
    check_label.config(text="")
    REPS=0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global REPS
    REPS+=1
    work_sec=WORK_MIN*60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60
    print(REPS)
    if REPS %8 ==0:
        title.config(text="LONG REST",fg=GREEN)
        count_down(long_sec)
    elif REPS%2==0:
        title.config(text="SHORT REST",fg=PINK)
        count_down(short_sec)
    else :
        title.config(text="WORK",fg=RED)

        count_down(work_sec)




def count_down(count):
    global timer
    min=math.floor(count/60)
    sec=count%60
    if sec <10:
        sec=f"0{sec}"

    canvas.itemconfig(timer_text,text=f"{min}:{sec}")
    if count>0:
      timer=  window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark=""
        for _ in range(math.floor(REPS/2)):
            mark+=CHECK_SYMBOL
            check_label.config(text=mark)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
fg=GREEN
window=Tk()
window.title("Pomodoro")
window.minsize(width=500,height=500)
window.config(padx=100,pady=50,bg=YELLOW)

title=Label(text="TIMER",font=(FONT_NAME,23,"bold"),fg=fg,bg=YELLOW)
title.grid(column=2,row=0)


canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,120,text=WORK_MIN,fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=2)


start_button=Button(text="Start",command=start_timer)
start_button.grid(row=2,column=1)

check_label=Label(fg=fg,background=YELLOW,font=(FONT_NAME,22,'bold'))
check_label.config(padx=4,pady=5)
check_label.grid(row=3,column=2)

reset_button=Button(text="Reset",command=time_reset)
reset_button.grid(row=2,column=3)






window.mainloop()


