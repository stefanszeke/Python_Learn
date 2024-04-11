import tkinter
from quiz_brain import QuizBrain
import os

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.window = tkinter.Tk()
        self.window.title = ("Quilzerr")
        self.quiz_brain = quiz_brain
        self.score = 0
        
        self.load_resources()
        self.create_layout()
    
        self._get_next_question()
        
        self.window.mainloop()
        
    def check_answer(self, answer):
        is_right = self.quiz_brain.check_answer(answer)
        self.update_ui(is_right)
        if is_right:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")


    def update_ui(self, isRight: bool):
        self.disable_buttons()
        self.canvas.config(bg="green" if isRight else "red")
        self.window.after(1000, self._get_next_question)
            
    def _get_next_question(self):
        self.canvas.config(bg="white"),
        if self.quiz_brain.still_has_questions():
            self.questions_label.config(text=f"# {self.quiz_brain.question_number + 1} / {len(self.quiz_brain.question_list)}")
            self.enable_buttons()
            question = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.canvas_text, text=question)
        else:
            self._complete_quiz()
            
    def _complete_quiz(self):
        self.canvas.itemconfig(self.canvas_text, text=f"You've completed the quiz, Your final score was: {self.score}/{self.quiz_brain.question_number}")

            
    def load_resources(self):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.btn_true_img_path = os.path.join(self.dir_path, 'images', 'true.png')
        self.btn_false_img_path = os.path.join(self.dir_path, 'images', 'false.png')
        self.btn_true_img = tkinter.PhotoImage(file=self.btn_true_img_path)
        self.btn_false_img = tkinter.PhotoImage(file=self.btn_false_img_path)
    
    def create_layout(self):
        self.window.config(pady=20, bg=THEME_COLOR)
        
        self.questions_label = tkinter.Label(text="#", bg=THEME_COLOR, fg="white", font=("Arial", 20, "bold"))
        self.questions_label.grid(row=0, column=2)
        
        self.score_label = tkinter.Label(text="Score 0", bg=THEME_COLOR, fg="white", font=("Arial", 20, "bold"))
        self.questions_label.config(text=f"# {self.quiz_brain.question_number+1} / {len(self.quiz_brain.question_list)}")
        self.score_label.grid(row=0, column=4)
        
        self.canvas = tkinter.Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas_text = self.canvas.create_text(150, 125, width=290, text="", fill="black",font=("Arial", 12, ))
        self.canvas.grid(row=1, column=2, columnspan=3 ,padx=20, pady=20  )
        

        self.button_true = tkinter.Button(text="true", highlightthickness=0, image=self.btn_true_img, command=lambda: self.check_answer("True"))
        self.button_false = tkinter.Button(text="false", highlightthickness=0, image=self.btn_false_img, command=lambda: self.check_answer("False"))
        self.button_true.grid(row=2, column=2,)
        self.button_false.grid(row=2, column=4)
        

    def disable_buttons(self):
        self.button_true.config(state="disabled")
        self.button_false.config(state="disabled")
        
    def enable_buttons(self):
        self.button_true.config(state="active")
        self.button_false.config(state="active")