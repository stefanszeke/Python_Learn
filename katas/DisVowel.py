def disemvowel(string_):
    arr = list(string_)
    noVowels = [x for x in arr if x.lower() not in ['a', 'e', 'i', 'o', 'u']]
    return ''.join(noVowels)

def disemvowel2(string_):
    return ''.join(x for x in string_ if x.lower() not in ['a', 'e', 'i', 'o', 'u'])

def disemvowel3(string_):
    for i in 'aeiouAEIOU':
        string_ = string_.replace(i,'')
    return string_


print(disemvowel("This website is for losers LOL!"))
print(disemvowel2("This website is for losers LOL!"))
print(disemvowel3("This website is for losers LOL!"))


# str = "This website is for losers LOL!"
# strt = ''.join(x for x in str if x.lower() not in ['a', 'e', 'i', 'o', 'u'])
# print(strt)                                                         