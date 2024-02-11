import random

# get the words from the list
words = ("banana", "banana")
selected_word = random.choice(words)
letters_left = "ABCDEFGHIJKLMNOPQRSTUVXYZ"

result = ["_" for ch in selected_word]
lives = 3

def printResult():
    print()
    print(letters_left)
    print(f'[ {" ".join(result)} ]  live: {lives}')
    
def guess(letter):
    found = False
    for i in range(0, len(selected_word)):
        if letter == selected_word[i]:
            result[i] = letter
            found = True
    return found

def replace(letter):
    return letters_left.replace(letter.upper(),"_")
            
def game():
    global lives
    global letters_left
    printResult()
    while True:
        user_input = input("Guess a letter: ")[0].lower()
        guessed = guess(user_input)
        print("Guessed: " + user_input)
        if not guessed:
            lives -= 1
        letters_left = replace(user_input)
        printResult()
        
        if lives < 1:
            print("game over")
            return
        if "_" not in result:
            print("you won !")
            return


game()