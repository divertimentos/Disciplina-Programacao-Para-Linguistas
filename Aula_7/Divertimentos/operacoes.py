print("Digite '0' para sair \n")

numero = 1
soma = 0
quantidade = 0

while numero != 0:
    numero = int(input("Digite números: \n"))
    if numero != 0:
        quantidade += 1
        soma  = soma + numero #Ou soma += numero
media = (soma / quantidade)

print("Quantidade:", quantidade)
print("Soma", soma)
print("media: %1.2f." %media)
