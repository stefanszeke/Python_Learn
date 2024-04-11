import tkinter as tk
import pandas as pd
import time

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

# Load File
wordsArray = []
words = None
try:
    words = pd.read_csv("data/Japanese_words_to_learn.csv")
except:
    words = pd.read_csv("data/Japanese_words.csv")   
wordsArray = words.to_dict(orient="records")

cur_index = 0
timer = None
timer_count = 0

def set_question():
    global cur_index
    canvas.itemconfig(card_title, text="Japanese")
    canvas.itemconfig(card_test, text=wordsArray[cur_index]["Japanese"])
    canvas.itemconfig(card, image=card_back)
    button_right.config(state="disabled")
    button_wrong.config(state="disabled")
    increment_timer()

def flip_card():
    global cur_index
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_test, text=wordsArray[cur_index]["English"])
    canvas.itemconfig(card, image=card_front)
    button_right.config(state="normal")
    button_wrong.config(state="normal")
    if(cur_index < len(wordsArray)-1):
        cur_index += 1
    else:
        cur_index = 0

def increment_timer():
    global timer_count
    timer_count += 1
    canvas.itemconfig(card_title, text=f'Japanese {timer_count}')

    if timer_count < 4:
        window.after(1000, increment_timer)
    else:
        flip_card()
        timer_count = 0
        
def remove_word():
    global cur_index
    wordsArray.pop(cur_index-1)
    cur_index -= 1
    

def save_progress():
    df = pd.DataFrame(wordsArray)
    df.to_csv("data/Japanese_words_to_learn.csv", index=False)

def set_finish():
    canvas.itemconfig(card_title, text="Well Done!")
    canvas.itemconfig(card_test, text="You have learned all the words", font=(FONT_NAME, 25, "bold"))
    canvas.itemconfig(card, image=card_back)
    button_right.config(state="disabled")
    button_wrong.config(state="disabled")
    df = pd.DataFrame(wordsArray)


def on_right():
    remove_word()
    save_progress()
    if(len(wordsArray) == 0):
        set_finish()
        return
    set_question()
    
def on_wrong():
    save_progress()
    set_question()

# window
window = tk.Tk()
window.title("Flash Cards")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)

# image card
canvas = tk.Canvas(width=900, height=570, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front = tk.PhotoImage(file="images/card_front.png")
card_back = tk.PhotoImage(file="images/card_back.png")

card = canvas.create_image(450, 300, image=card_back)
card_title = canvas.create_text(450, 150, text="Japanese", fill="black", font=(FONT_NAME, 40, "italic"))
card_test = canvas.create_text(450, 300, text=wordsArray[0]["Japanese"], fill="black", font=(FONT_NAME, 45, "bold"))
canvas.grid(row=1, column=2, columnspan=3 ,  )


# buttons
button_right_icon = tk.PhotoImage(file="images/right.png")
button_right = tk.Button(text="Right", highlightthickness=0, image=button_right_icon, command=on_right, state="disabled")
button_right.grid(row=2, column=2)

button_wrong_icon = tk.PhotoImage(file="images/wrong.png")
button_wrong = tk.Button(text="Wrong", highlightthickness=0, image=button_wrong_icon, command=on_wrong, state="disabled")
button_wrong.grid(row=2, column=4)

set_question()
window.mainloop()

