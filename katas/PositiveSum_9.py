def positive_sum(arr):
    positiveArr = [x for x in arr if x > 0]
    sum = 0
    for x in positiveArr:
        sum += x
        
    return sum if sum > 0 else 0

def positive_sum2(arr):
    return sum(filter(lambda x: x > 0, arr))

def positive_sum3(arr):
    return sum(x for x in arr if x > 0)

positive_sum4 = lambda arr: sum(x for x in arr if x > 0)

arr = [1, -2, 3, -4, 5, 6, -7, 8, -9]

print(positive_sum(arr))
print(positive_sum2(arr))
print(positive_sum3(arr))
print(positive_sum4(arr))