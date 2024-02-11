test_input = '  cat   dog '
test_input2 = 'Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'



def generate_hashtag(s):
    result = "#"+"".join(x.title() for x in s.split())
    return len(result) <= 140 and result != "#" and result or False

print(generate_hashtag(test_input))



def generate_hashtag2(s):
    result = "#"
    for x in s.split():
        result += x.title()
    return len(result) <= 140 and result != "#" and result or False

print(generate_hashtag2(test_input))