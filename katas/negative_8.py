def make_negative( number ):
    return abs(number) * -1

def make_negative2( number ):
    return number if number < 0 else -number
    
print(make_negative(8))
print(make_negative(-42))

print(make_negative2(8))
print(make_negative2(-42))
