import random
import time
from rockPaper import painter

def get_player_selection():
    while True:
        selection = input('Enter rock(1), paper(2), or scissors(3): ')
        if selection.isdigit() and int(selection) in [1,2,3]:
            return rps[int(selection)-1]
        elif selection.lower() in ['rock', 'paper', 'scissors']:
            return selection.lower()
        else:
            print('Please enter a valid selection.')

def get_ai_selection():
    return rps[random.randint(0,2)]

def determine_outcome(player, ai):
    if player == ai:
        return "It's a draw"
    elif (player == 'rock' and ai == 'scissors') or \
         (player == 'scissors' and ai == 'paper') or \
         (player == 'paper' and ai == 'rock'):
        return 'You win'
    else:
        return 'You lose'

def game():
    playerScore = 0
    aiScore = 0
    gameOn = True

    while gameOn:
        print("Game started")
        # Get selections
        player_selection = get_player_selection()
        print(f'-> You selected {player_selection}')
        painter(player_selection)  # Assuming you have a painter function to visually represent the choice

        ai_selection = get_ai_selection()
        time.sleep(1)
        print(f'AI selected {ai_selection}')
        painter(ai_selection)  # Similarly for the AI's choice

        time.sleep(1)
        
        outcome = determine_outcome(player_selection, ai_selection)
        print(outcome)

        time.sleep(1)
        
        # Update scores
        if outcome == 'You win':
            playerScore += 1
        elif outcome == 'You lose':
            aiScore += 1

        print(f'Player score: {playerScore} | AI score: {aiScore}\n')

        # Check if playing again
        again = input('Play again? (yes or no): ').lower()
        if again == 'no':
            print("Ending game")
            print('Thanks for playing')
            print(f'Final score: Player: {playerScore} AI: {aiScore}')
            if playerScore > aiScore:
                print('You won!')
            elif playerScore < aiScore:
                print('You lost!')
            else:
                print('\nIt was a draw!')
            gameOn = False
            break
        elif again != 'yes':
            print('Please enter valid selection.')
    print("Game loop exited")

# Assuming these are defined
rps = ['rock', 'paper', 'scissors']
game()
