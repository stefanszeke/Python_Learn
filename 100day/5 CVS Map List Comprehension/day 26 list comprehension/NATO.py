import pandas

nato_abc = pandas.read_csv('nato_phonetic_alphabet.csv')


nato_abc_dict = {row.letter:row.code for (index, row) in nato_abc.iterrows()}


def get_nato_word_by_letter(letter) -> str:
    return nato_abc_dict[letter.upper()]


def get_nato_full(word):
    return [get_nato_word_by_letter(ch) if ch.isalpha() else "-" for ch in word ]

def get_nato_with_exception(word):
    return [get_nato_word_by_letter(ch) for ch in word ]

# test_input = 'Stefan Szekely'

# result = get_nato_full(test_input)
# print(result)


def generate_with_exception():
    word = input("Enter a word: ")
    try:
        result = get_nato_with_exception(word)
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_with_exception()
    else:
        print(result)
        
generate_with_exception()