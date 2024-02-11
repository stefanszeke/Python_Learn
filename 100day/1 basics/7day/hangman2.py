import random

class HangmanGame:
    def __init__(self):
        self.words = ("banana", "banana")
        self.selected_word = random.choice(self.words)
        self.result = ["_" for ch in self.selected_word]
        self.lives = 3
        self.letters_left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.guessed_letters = set()
        
        
    
    def print_result(self):
        print()
        print(' '.join(self.letters_left))
        print(f'[ {" ".join(self.result)} ]  lives: {self.lives}')
        
    def guess(self, letter):
        if letter in self.selected_word:
            for i, let in enumerate(self.selected_word):
                if let == letter:
                    self.result[i] = letter
            return True
        else:
            return False
        
    def game(self):
        self.print_result()
        while True:
            user_input = input("Guess a letter: ")[0].lower()
            if(user_input in self.guessed_letters):
                print("You have already tried this letter")
                continue
            if(user_input.upper() not in self.letters_left or user_input == "_"):
                print("Wrong input type")
                continue
            
            self.guessed_letters.add(user_input)
            self.letters_left = self.letters_left.replace(user_input.upper(), "_")
            
            if not self.guess(user_input):
                self.lives -= 1
            
            self.print_result()
            
            if self.lives < 1:
                print("game over,")
                return
            if "_" not in self.result:
                print("you won !")
                return
    
    
if __name__ == "__main__":
    game_instance = HangmanGame()
    game_instance.game()