import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLUE = "#a7d129"
FONT_NAME = "Courier"
WORK_MIN = 25*60
SHORT_BREAK_MIN = 5*60
LONG_BREAK_MIN = 20*60

count = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global count
    count = 0
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    window.after_cancel(timer)
    label.config(text="Timer", fg=GREEN)
    
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global count
    print(f'count: {count}')
        
    
    if(count == 16):
        label.config(text="COMPLETE", fg=BLUE)
        return
    if(count == 7):
        count_down(LONG_BREAK_MIN)
        label.config(text="Long Break", fg=RED)
        check_marks.config(text=check_marks.cget("text") + "✔")
    elif(count % 2 == 0):
        label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN)
    else:
        label.config(text="Break", fg=PINK)
        check_marks.config(text=check_marks.cget("text") + "✔")
        count_down(SHORT_BREAK_MIN)
        
    count += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    
    min = math.floor(count / 60)
    sec = count % 60

    new_time = f"{min:02d}:{sec:02d}"
    canvas.itemconfig(timer_text, text=new_time)
    
    if(count > 0):
        timer = window.after(1000, count_down, count - 1)
    else:
        print("Time's up")
        start_timer()

    



# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



# label
label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, width=10, font=(FONT_NAME, 50, "bold"))
label.grid(row=0, column=1)

# image
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tk.PhotoImage(file="tomato.png")

canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 45, "bold"))
canvas.grid(row=1, column=1)


# buttons
start_button = tk.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tk.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# check marks
check_marks = tk.Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
check_marks.grid(row=2, column=1)

window.mainloop()
