testInput = "Ttttthe quick brown fox jumps over the lazy dog!"
testInput2 = "abcdefghijklmnopqrstuvqxyz"

def is_pangram(s):
    array = []
    for i in s:
        if i.isalpha():
            if i.lower() not in array:
                array.append(i.lower())
    return len(array) == 26


def is_pangram2(s):
    return len(set([x for x in s.lower() if x.isalpha()])) == 26

def is_pangram3(s):
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in s.lower():
            return False
    return True


# print(is_pangram(testInput))
print(is_pangram2(testInput2))
print(is_pangram3(testInput2))