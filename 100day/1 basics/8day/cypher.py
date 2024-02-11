from logo import logo

def getNewLetter(letter, num, encode):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    
    if letter not in abc:
        return letter

    if not encode:
        abc = "".join(reversed(abc))
    
    start = abc.index(letter)
    return abc[(num+start)%len(abc)]
    



def cipher(word, num, encode):
    return "".join([getNewLetter(x, num , encode) for x in word])

print(logo)

def cipher_app():
    end = False
    
    while not end:
        options = ("Decode", "Encode")
        toEncode = "s"
        while toEncode[0].lower() not in ("e","d"):
            toEncode = input("Do you want to Encode(e) or Decode(d) ?\n")
            if toEncode[0].lower() not in ("e","d"):
                print("try again")
        encode = True if toEncode[0].lower() == "e" else False
        print(options[encode])
        
        word = input(f'type word to {options[encode]}\n' )
        
        while True:
            step = input("type in number of steps\n")
            if not step.isdigit():
                step = input("try again: type in number of steps\n")
            else:
                break
        result = cipher(word, int(step), encode)
        print(result)
        
        again = input("want to try again y/n: ")
        if again != 'y':
            end = True

cipher_app()