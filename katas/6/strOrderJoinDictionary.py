testInput1 = "is20 Thi1s T48000est 3453a"

def getDigit(text):
    return int("".join(x for x in text if x.isdigit()))

def order(sentence):
    words_dict = {}
    for word in sentence.split(" "):
        key = getDigit(word)
        words_dict[key] = word
        
    return " ".join([words_dict[key] for key in sorted(words_dict.keys())])


print(order(testInput1))





