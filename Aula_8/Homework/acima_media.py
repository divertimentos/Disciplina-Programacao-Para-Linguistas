notas = []

for i in range(3):
    notas.append(float(input("Digite uma nota: \n"))) #Dá pra fazer adicionar itens à lista usando input() em apenas uma linha.
media = ((notas[0] + notas[1] + notas[2]) / 3)
print("A média de notas é: %3.2f." %(media))

for i in range(3):
    if notas[i] > media:
        print("Acima da média:", notas[i])
