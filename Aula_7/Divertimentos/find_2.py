string = "martelo."
substring = "te"
pos = (string.find(substring))

print(string[0 : string.find(substring)].capitalize(), end = "")
print(string[pos : pos + len(substring)].upper(), end = "")
print(string[pos + len(substring) : len(string)], end = "")
