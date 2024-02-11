
letter = ''
names = []


# read letter
with open('./letter/letter.txt', 'r') as file:
    letter = file.read()
    
# read names
with open('./names/names.txt', 'r') as file:
    for name in file.readlines():
        names.append(name.strip())
    
# create letter for each name    
for name in names:
    with open(f'./output/letter_for_{name}.txt', 'w') as file:
        file.write(letter.replace('[name]', name))
        
print(letter)