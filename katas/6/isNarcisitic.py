def narcissistic( value ):
    x = len(str(value))
    numbs = sum([int(y)**x for y in str(value)])
    return numbs == value


print(narcissistic(7))