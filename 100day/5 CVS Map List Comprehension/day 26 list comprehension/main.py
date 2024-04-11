


def get_word_from_letter(letter):
    difference = ord('a')
    abc = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india', 'juliett', 'kilo', 'lima', 'mike', 'november', 'oscar', 'papa', 'quebec', 'romeo', 'sierra', 'tango', 'uniform', 'victor', 'whiskey', 'x-ray', 'yankee', 'zulu']
    return abc[ord(letter) - difference]


def get_abc_words(name):
    return [get_word_from_letter(ch.lower()).title() for ch in name if ch.isalpha()]




def main():
    name = input("Enter your name: ")
    print(get_abc_words(name))
    
if __name__ == "__main__":
    main()
    


    
    

