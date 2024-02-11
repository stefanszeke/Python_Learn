import pandas

nato_abc = pandas.read_csv('nato_phonetic_alphabet.csv')


nato_abc_dict = {row.letter:row.code for (index, row) in nato_abc.iterrows()}


def get_nato_word(letter) -> str:
    return nato_abc_dict[letter.upper()]


def get_nato_full(word):
    return [get_nato_word(ch) if ch.isalpha() else "-" for ch in word ]

test_input = 'Stefan Szekely'

result = get_nato_full(test_input)
print(result)