turma = {}
counter = 0

for i in range(3):
    nome = input("Digite um nome: \n")
    if nome == "-1":
        break
    nota = float(input("E sua nota: \n"))
    turma[nome] = nota #Adiciona 'nota' à chave 'nome' dentro do dicionário 'turma'
    counter += nota #somador das notas

media = counter / 3
print("A média é:", media)

for nome in turma.keys(): # Escrever no papel pra entender como funciona esse bloco
    if turma[nome] > media:
        print("Parabéns,", nome)
