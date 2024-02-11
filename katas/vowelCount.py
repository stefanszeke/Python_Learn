def get_count(sentence):
    cont = 0
    for letter in sentence:
        if letter in 'aeiou':
            cont += 1
    return cont

def get_count2(sentence):
    return len([c for c in sentence if c in 'aeiou'])

def get_count3(sentence):
    return sum(c in 'aeiou' for c in sentence)

def get_count4(sentence):
    return sum(1 for c in sentence if c in 'aeiou')

sentence = "ghagfhgefhfghfaajfghfghgfhie"

print(get_count(sentence))
print(get_count2(sentence))
print(get_count3(sentence))
