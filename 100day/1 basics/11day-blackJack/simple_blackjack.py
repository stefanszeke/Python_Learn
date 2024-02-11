
import random
import os
import time

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
choices = {'s': 'Stand', 'h': 'Hit'}

player_cards = []
computer_cards = []
player_money = 0

def calculate_total(cards):
    total = sum(cards)
    if total > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        total = sum(cards)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_total(cards):
    calculate_total(cards)
    return sum(cards)

def print_game(show_computer_cards=False):
    calculate_total(player_cards)
    calculate_total(computer_cards)
    print(f'[ Your total: {get_total(player_cards)}, cards: {player_cards} ] money: {player_money}€')
    if show_computer_cards:
        print(f'[ Comp total: {get_total(computer_cards)}, cards: {computer_cards} ]')
    else:
        print(f'[ Computer\'s first card: {computer_cards[0]} ]')
    
def get_card():
    return random.choice(cards)


def get_choice():
    choice = ''
    while True:
        choice = input('Type Stand(s) or Hit(h): ')
        if choice[0].lower() in ['s', 'h']:
            print(f'[ {choices[choice[0].lower()]} ]')
            break
        else:
            print('Invalid input')
    return choice



def game():
    global player_money
    game_on: bool = True
    stand: bool = False
    round_on: bool = True
    won_round: bool = False
    while game_on:
        for _ in range(2):
            computer_cards.append(get_card())
        player_cards.append(get_card())
        player_cards.append(11)
            
        
        print_game()
        time.sleep(1)
        while(get_total(player_cards) < 21 and not stand):
            clear_console()
            print_game()
            choice = get_choice()
            time.sleep(1)
            if(choice == 's'):
                stand = True
            else:
                card = get_card()
                player_cards.append(card)
                print(f'You HIT: [{card}]')
                time.sleep(1)

        if(get_total(player_cards) == 21):
            print('You win! [Blackjack]')
            won_round = True
            round_on = False

            
        if(get_total(player_cards) > 21):
            print('You lost!')
            round_on = False

        time.sleep(1)
        clear_console()


        if round_on:
            print('Computer turn')
            print_game(True)
            time.sleep(1)
            while(get_total(computer_cards) < get_total(player_cards) and get_total(computer_cards) <= 21):
                card = get_card()
                computer_cards.append(card)
                print(f'Computer HIT: [{card}]')
                time.sleep(1)
                print_game(True)
            else:
                if get_total(computer_cards) > 21:
                    print('You win!')
                    round_on = False
                    won_round = True
                else:
                    print('computer stand')
                time.sleep(1)
        else:
            print_game(True)
            time.sleep(1)
        
        if round_on:
            if(get_total(computer_cards) == 21):
                print('You lost! [Blackjack]')
            elif(get_total(computer_cards) == get_total(player_cards)):
                print('Draw!')
            elif(get_total(computer_cards) > get_total(player_cards) and get_total(computer_cards) <= 21):
                print('You lost!')
            elif(get_total(computer_cards) < 21 and get_total(computer_cards) < get_total(player_cards)):
                print('You win!')
                won_round = True
            
        if won_round:
            player_money = 10 if player_money == 0 else player_money * 2
            print(f'You have {player_money}€')
        else:
            player_money = 0
            print(f'Your money has been lost: {player_money}€')
            
        print("new Game? (y/n)")
        if input().lower() == 'y':
            player_cards.clear()
            computer_cards.clear()
            stand = False
            round_on = True
            won_round = False
            clear_console()
        else:
            game_on = False
            break           

        
game()