import random

string = "abcd"
array = list(string)
random.shuffle(array)

string = "".join(array)

print(string)

array2 = ["e","f","g","g"]

joined = list(string) + array2

print(joined)