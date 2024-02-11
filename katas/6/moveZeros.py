def move_zeros(lst):
    for n in lst:
        if n == 0:
            lst.remove(n)
            lst.append(n)
    return lst


test_input = [0, 1, 0, 3, 12]
print(move_zeros(test_input))