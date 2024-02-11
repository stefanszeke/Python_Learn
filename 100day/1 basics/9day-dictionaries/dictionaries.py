people = {

}

people = {
    'Alice': {'age': 30, 'salary': 8000},
    'Bob': {'age': 25, 'salary': 5000},
    'Charlie': {'age': 35, 'salary': 4000},
    'jack': {'age': 33, 'salary': 6000}
}

for key, value in people.items():
    print(f'{key} is {value["age"]} years old and earns {value["salary"]} dollars')
    
print()

# sort by age
sorterByAge = sorted(people.items(), key=lambda value: value[1]['age'], reverse=True)

for key, value in sorterByAge:
    print(f'{key} is {value["age"]} years old and earns {value["salary"]} dollars')