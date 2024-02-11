
test_input = "AAAABBBCCDAABBB"

def unique_in_order(sequence):
    result = []
    for i in range(len(sequence)):
        if i == 0:
            result.append(sequence[i])
        elif sequence[i] != sequence[i-1]:
            result.append(sequence[i])
            
    return result

print(unique_in_order(test_input))