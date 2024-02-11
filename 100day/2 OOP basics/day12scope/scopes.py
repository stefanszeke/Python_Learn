num = 1

def increase_num():
    num = 20
    print(f"num in function: {num}")
    
increase_num()
print(f"num outside function: {num}")

def increase_num():
    global num
    num = 30
    print(f"num in function: {num}")
    
increase_num()

def increase_num2():
    return num + 1

print(f"num outside function: {num}")
num = increase_num2()
print(f"num outside function: {num}")

# global constants
PI = 3.14
GRAVITY = 9.8

def get_circle_area(radius):
    return PI * radius * radius
