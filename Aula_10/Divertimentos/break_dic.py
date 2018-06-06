turma = {}

while True:
    nome = (input("Nome do aluno: \n"))
    if nome == "-1":
        break
    nota = float(input("Nota: \n"))
    turma[nome] = nota # Ainda não entendi como esta operação funciona. Por que [nome] refere-se a um float e não a um nome?
print(turma)

maior = -1
melhor = " "

for nome in turma.keys():
    if turma[nome] > maior:
        maior = turma[nome]
        melhor = nome
print("Parabéns,",melhor)
