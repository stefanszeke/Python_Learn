class QuizBrain:
    
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.current_question = None
        self.score = 0
        
    def nextQuestion(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        
        self.user_answer = input(f"Q.{self.question_number}: {self.current_question.text} (True/False): ")
        while not self.isValidInput():
            self.user_answer = input(f"Q.{self.question_number}: {self.current_question.text} (True/False): must be True or False: ")
            
        self.checkAnswer()
        
    def checkAnswer(self):
        if self.user_answer.lower() == self.current_question.answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
            
    def isValidInput(self):
        return self.user_answer.lower() in ["true", "false"]
    
    def stillHasQuestions(self):
        return self.question_number < len(self.question_list)
    
    def printScore(self):
        print(f"Your final score was: {self.score}/{self.question_number}")
        
    def start(self):
        while self.stillHasQuestions():
            self.nextQuestion()
        self.printScore()
