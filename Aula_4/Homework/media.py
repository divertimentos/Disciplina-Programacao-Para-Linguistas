num1 = input("Insira o primeiro número: \n")
num2 = input("Insira o segundo número: \n")

print((int(num1) + int(num2)) / 2)

#O programa calculou corretamente a média porque os parênteses foram posicionados de forma a somar antes de dividir. Caso contrário, o Python dividiria num2 por 2 e, em seguida, somaria num1 a 2.
