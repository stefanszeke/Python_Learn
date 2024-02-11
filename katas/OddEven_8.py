def even_or_odd(number):
    
    if(type(number) != int):
        return "Not an integer"
    print("Number: ", number)
    print("number % 2: ", number % 2)
    
    return 'Odd' if number % 2 else 'Even'

def even_or_odd2(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
    
def even_or_odd3(number):
    return ['Even', 'Odd'][number % 2]

a = 8

print(even_or_odd(a))
# print(even_or_odd2(a))
# print(even_or_odd3(a))





    