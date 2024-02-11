def sum_two_smallest_numbers(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[0] + sorted_numbers[1]

numbs1 = [1,2,3,11,4,5,6,10,9,21]

def sum_two_smallest_numbers2(numbers):
    return sum(sorted(numbers)[:2])

print(sum_two_smallest_numbers(numbs1))
print(sum_two_smallest_numbers2(numbs1))




def name_value(d):
    return d['name']

dicts = [{'name': 'John', 'age': 15}, {'name': 'Doe', 'age': 30}, {'name': 'Alice', 'age': 25}]
dicts.sort(key=name_value)
print(dicts)  # Output: [{'name': 'Alice', 'age': 25}, {'name': 'Doe', 'age': 30}, {'name': 'John', 'age': 15}]



def second_element(t):
    return t[1]

tuples = [(1, 2), (3, 1), (4, 5), (2, 3)]
tuples.sort(key=second_element)
print(tuples)  # Output: [(3, 1), (1, 2), (2, 3), (4, 5)]



def last_letter(s):
    return s[-1]

words = ['apple', 'banana', 'cherry', 'date', "kiwi", 'mango', 'banana']
words.sort(key=last_letter)
print(words)  # Output: ['banana', 'apple', 'date', 'cherry']
