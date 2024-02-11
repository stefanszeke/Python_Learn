print('''
                             'Xx  xX*,
                          ,*xXXx_xXx
                            _xXXXXXxx*,
                          ,*XXx@x@Xx
                            X @|@@ `x
                            '  ||    '
                               ||
                               ||
                               ||
                               ||
                            /ssssssss.
                      /sssssssSSSSssssssssss.
        /\         /sssssSSSSSSSSSSSSSSSssssssssssss.             
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
''')


def game_loop():
    
    gameover = False
    direction = ''
    action1 = ''
    action2 = ''

    while not gameover:
        
        while direction != 'left' and direction != 'right':
            direction = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' \n").lower()
            if direction == 'left':
                action1 = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. \n").lower()
            elif direction == 'right':
                print("You fell into a hole. Game Over.")
                return
            else:
                print("You didn't choose a direction. Try again.")
            
        while action1 != 'wait' and action1 != 'swim':
            action1 = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. \n").lower()
            if action1 == 'wait':
                action2 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
            elif action1 == 'swim':
                print("You got attacked by an angry trout. Game Over.")
                gameover = True
                return
            else:
                print("You didn't choose an action. Try again.")

game_loop()