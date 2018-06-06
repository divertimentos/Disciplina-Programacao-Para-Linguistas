string = input("Digite uma string a ser revertida: \n")
for i in reversed(range(0, len(string))):
    print(string[i], end = "")
