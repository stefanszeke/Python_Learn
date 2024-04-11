def add1(*nums):
    print(type(nums))
    return sum(num for num in nums if isinstance(num, (int, float)))


def add2(*nums):
    total = 0
    for num in nums:
        try:
            total += float(num)
        except ValueError:
            continue
    return total

print(add1(1, 1, "3", 1, "f"))
print(add2(1, 1, "3", 1, "f"))



def calculate(start = 0, **kwargs):
    print(type(kwargs))
    print(kwargs)
    
    result = start
    result += kwargs.get("add", 0)
    result *= kwargs.get("multiply", 1)
    return result
    
print(calculate(add=3, multiply=5))

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")