# import random
# import time
def painter(selection):
    if selection == 'rock':
        print('''
                _______
            ---'   ____)
                (_____)
                (_____)
                (____)
            ---.__(___)
            ''')
    elif selection == 'paper':
        print('''
                _______
            ---'   ____)____
                    ______)
                    _______)
                    _______)
            ---.__________)
            ''')
    elif selection == 'scissors':
        print('''
                _______
            ---'   ____)____
                    ______)
                __________)
                (____)
            ---.__(___)
            ''')
# rps = ['rock', 'paper', 'scissors']
# outcomes = {
#     'rock': {'rock': 'Its a draw', 'paper': 'You lose', 'scissors': 'You win'},
#     'paper': {'rock': 'You win', 'paper': 'Its a draw', 'scissors': 'You lose'},
#     'scissors': {'rock': 'You lose', 'paper': 'You win', 'scissors': 'Its a draw'},
# }

# def game():

#     playerScore = 0
#     aiScore = 0
#     selection = ''
#     endGame = False

#     while not endGame:
#         while True:
#             selection = input('Enter rock(1), paper(2), or scissors(3): ')
#             if selection.isdigit() and int(selection) in [1,2,3]:
#                 break
#             elif selection.lower() in ['rock', 'paper', 'scissors']:
#                 break
#             else:
#                 print('Please enter valid selection')

#         selection = rps[int(selection)-1] if selection.isdigit() else selection.lower()

#         print(f'You selected {selection}')
#         painter(selection)

#         ai_selection = random.randint(1,3)
#         ai_selection = rps[ai_selection-1]

#         time.sleep(1)

#         print(f'AI selected {ai_selection}')
#         painter(ai_selection)

#         time.sleep(1)
#         outcome = outcomes[selection][ai_selection]
        
#         print(outcome)
        
#         if(outcome == 'You win'):
#             playerScore += 1
#         elif(outcome == 'You lose'):
#             aiScore += 1
            
#         print(f'Player score: {playerScore}')
#         print(f'AI score: {aiScore}')
        
#         print('-------------------')
        
#         print('Play again?')
#         again = ""
        
#         while again not in ['yes', 'no']:
#             again = input('Enter yes or no: ')
#             if again == 'no':
#                 endGame = True
#                 print('Thanks for playing')
#                 print(f'Final score: Player: {playerScore} AI: {aiScore}')
#                 if(playerScore > aiScore):
#                     print('You won!')
#                 elif(playerScore < aiScore):
#                     print('You lost!')
#                 else:
#                     print('Its was a draw!')
                    
#                 break
#             elif again == 'yes':
#                 break
#             else:
#                 print('Please enter valid selection')
                
# game()
            
        
    
