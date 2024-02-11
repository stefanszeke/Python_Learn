import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

bidders = {}

while True:
    clear_console()
    name = input('Enter your name: ')
    bid = int(input('Enter your bid: '))
    bidders[name] = bid
    
    more = input('More bidders? (y/n) ')
    if more == 'n':
        break


    
clear_console()

sortedBidders = sorted(bidders.items(), key=lambda value: value[1], reverse=True)

highestBid = sortedBidders[0]

print(f'The winner is {highestBid[0]} with a bid of {highestBid[1]} dollars')