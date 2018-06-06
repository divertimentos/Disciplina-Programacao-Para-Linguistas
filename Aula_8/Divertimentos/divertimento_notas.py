notas = []
nomes = []

for i in range(3):
    nome = input("Digite um nome: \n")
    entrada = float(input("Digite a nota de %s \n" %(nome)))
    notas.append(entrada)
media = ((notas[0] + notas[1] + notas[2]) / 3)
print("Média:", media)

for i in range(3):
    if notas[i] > media:
        print("Parabéns,", nomes[i]) #Por que esta linha deu pau?
