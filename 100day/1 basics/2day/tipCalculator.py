print("Welcome to tip calculator")

total = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip = 0
while tip not in [10,12,15]:
    try:
        tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
        if tip not in [10,12,15]:
            print("Please enter valid number: 10, 12, 15")
    except ValueError:
        print("Please enter valid number")


totalWithTip = total + (total/100*tip)
each = totalWithTip/people

print(f'type of each: {type(each)}')
if(type(each) == float):
    print(f'its a float')

print(f'Each person should pay ${round(each, 1)}')