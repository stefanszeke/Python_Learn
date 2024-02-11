test_input1 = 'moonmen'
test_input2 = 'moonmEn'

def first_non_repeating_letter(s):
    for c in s:
        if s.lower().count(c.lower()) == 1:
            return c
        
    return ''

print(first_non_repeating_letter(test_input1))
print(first_non_repeating_letter(test_input2))

