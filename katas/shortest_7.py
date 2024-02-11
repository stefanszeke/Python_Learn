import re

str1 = "bitcoin take over  the world     maybe who knows perhaps dfgd fgdfgdfgdfgdfg"

def find_short(s):
    # your code here
    return sorted([len(x) for x in s.split(" ")])[0]

# print(find_short(str1))



def find_short2(s):
    splited = re.split(r' +', s)
    print("splitted:", splited)

    mappedToLength = [len(x) for x in splited]
    print("mappedToLength:", mappedToLength)
    
    sortedArr = sorted(mappedToLength)
    print("sortedArr:", sortedArr)
    
    lowestNumber = sortedArr[0]
    print("lowestNumber:", lowestNumber)
    
    return lowestNumber
    
print(find_short2(str1))
