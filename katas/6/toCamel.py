testInput1 = "the-stealth-warrior"
testInput2 = "The_Stealth_Warrior"
import re

def to_camel_case(text):
    splitted_text = re.split(r'[-_]', text)
    for i in range(1, len(splitted_text)):
        splitted_text[i] = splitted_text[i].capitalize()
    return ''.join(splitted_text)

print(to_camel_case(testInput2))