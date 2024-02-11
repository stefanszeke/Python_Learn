import random
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*()_+"

result = ''

def addToString(str, add, index):
    return str[:index] + add + str[index:]

def generatePassword(l,n,s):
    result = ''
    for i in range(0,l):
        result += letters[random.randint(0,len(letters)-1)]
    for i in range(0,n):
        random_number = numbers[random.randint(0, len(numbers)-1)]
        random_index = random.randint(0, len(result)-1)
        result = addToString(result, random_number, random_index)
    for i in range(0, s):
        random_symbol = symbols[random.randint(0, len(symbols)-1)]
        random_index = random.randint(0, len(result)-1)
        result = addToString(result, random_symbol, random_index)
        
    return result

print(generatePassword(3,1,1))