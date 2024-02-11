instString = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

result = ":".join([str(int(n)*100) for n in instString if int(n) > 5])

print(result)


for i,n in enumerate(instString):
    print(f'index: {i} = {n}')