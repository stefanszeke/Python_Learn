names = ["Ryan", "Kieran", "Mark"]

def friend(names):
    return [name for name in names if (len(name) == 4)]


print(friend(names))