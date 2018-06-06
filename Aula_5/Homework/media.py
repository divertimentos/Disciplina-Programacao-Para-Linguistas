num1 = float(input("Digite o primeiro número: \n"))
num2 = float(input("Digite o segundo número: \n"))
num3 = float(input("Digite o terceiro número: \n"))
soma_num = (num1 + num2 + num3)
resultado = (soma_num / 3)
print("A média é: %s" %resultado)

if resultado >= 6 and resultado < 11:
    print("Aprovado.")
elif resultado >= 5 and resultado <= 6:
    print("De REC.")
elif resultado < 5:
    print("Reprovado.")
else:
    print("O resultado é maior do que 10.")
