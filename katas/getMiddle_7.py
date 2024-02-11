def get_middle(s):
    i1 = (len(s)-1)//2
    i2 = len(s)//2+1
    print(f'i1 = {i1}, i2 = {i2}')
    return s[i1:i2]

def get_middle2(s):
    i1 = (len(s)//2 if len(s)%2 != 0 else (len(s)-1)//2)
    i2 = len(s)//2+1
    print(f'i1 = {i1}, i2 = {i2}')
    return s[i1:i2]
    

# len = 4 - 1 = 3 // 2 = 1
# len = 4 // 2 + 1 = 3 // 
str1 = "*****test*****"
str2 = "*****testing*****"

print(get_middle(str1))
print(get_middle2(str1))

print(get_middle(str2))
print(get_middle2(str2))

# len = 7 - 1 = 6 // 2 = 3
# len = 7 // 2 + 1 = 4

# print()

# s1 = "*****MM*****" # 12/2 = 6
# s2 = "******M******" # 13/2 = 6.5
# print(s1[5:7])
# print(s2[6:7])