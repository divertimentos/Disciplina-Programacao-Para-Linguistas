num = int(input("Digite um número positivo: \n"))

if (num <= 0):
    while (num <= 0):
        print("O número %s é negativo. Por favor, insira um número positivo." %num)
        num = int(input("Digite um número positivo: \n"))
else:
    print("O número %s é positivo. Parabéns." %num)
