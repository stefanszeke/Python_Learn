
str1 = "The narwhal bacons at midnight."
abc = "abcdefghijklmnopqrstuvwxyz"

print(abc.index("a"))

def alphabet_position(text):
    return ' '.join([str(abc.index(x.lower())+1) for x in text if x.lower() in abc])


result = alphabet_position(str1)
print(result)