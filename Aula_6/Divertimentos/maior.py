n = 0
maior = n

while n != -1:
    n = int(input("Digite um número: \n"))
    if n > maior:
        maior  = n
if maior > 0:
    print("O maior é: %s." %maior)
else:
    print("Nenhum número fornecido.")
