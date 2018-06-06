entrada = input("Digite uma string a ser printada no formato escada: \n")
entrada = entrada.upper()
for i in range(0, len(entrada)):
    print(entrada[0:i + 1])
