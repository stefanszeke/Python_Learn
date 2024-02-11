string = "Hello, World!"
char = "o"

indices = [i for i, c in enumerate(string) if c == char]
print(f"Indices of '{char}' are:", indices)
