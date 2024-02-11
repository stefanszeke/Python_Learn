fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

fruits_dict = {fruit: len(fruit) for fruit in fruits}

print(fruits_dict)

new_fruits = {k.title(): v*10 for k, v in fruits_dict.items() if v > 5}

print(new_fruits)