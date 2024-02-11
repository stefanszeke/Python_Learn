import random

def generate_password2(num_letters, num_numbers, num_symbols):
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+"
    
    password_chars = (
        [random.choice(letters) for _ in range(num_letters)] +
        [random.choice(numbers) for _ in range(num_numbers)] +
        [random.choice(symbols) for _ in range(num_symbols)]
    )
    
    random.shuffle(password_chars)
    return ''.join(password_chars)

# print(generate_password2(3, 1, 1))

list1 = ["1", 2, 3, 4, 5, 6, "7", 8, 9]
randomChoice = [random.choice(list1) for _ in range(3)]
print(randomChoice)

largerThan5 = [int(x)*100 for x in list1 if int(x) > 5]
print(largerThan5)