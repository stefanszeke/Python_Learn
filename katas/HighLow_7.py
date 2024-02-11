def high_and_low(numbers):
    numbs = [int(x) for x in numbers.split(" ")]

    highest = max(numbs)
    lowest = min(numbs)
    return str(highest) + " " + str(lowest)

testNumbs = "8 3 -5 42 -1 0 0 -9 4 7 4 -4"

print(high_and_low(testNumbs))

