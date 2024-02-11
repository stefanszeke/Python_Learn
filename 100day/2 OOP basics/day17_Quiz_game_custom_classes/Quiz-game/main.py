from data import question_data, question_data2
from question_model import Question
from quiz_brain import QuizBrain
import html


question_bank = [Question(html.unescape(question["question"]), question["correct_answer"]) for question in question_data2['results']]


    
print(*[f"Question: {q.text}, Answer: {q.answer}" for q in question_bank], sep="\n")

quiz = QuizBrain(question_bank)

quiz.start()
