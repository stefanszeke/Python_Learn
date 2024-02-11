

def getIndex(start, steps):
    word = "abcd"
    print(f'modulo: {steps+start} % {len(word)} = ', (steps+start)%len(word))
    return word[(steps+start)%len(word)]
    



for i in range(0,20):
    print(f'i: {i} ', getIndex(2, i))