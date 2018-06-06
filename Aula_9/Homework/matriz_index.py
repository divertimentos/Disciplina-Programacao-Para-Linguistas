turma = [[5.0, 4.5, 7.0, 5.2, 6.1], [2.1, 6.5, 8.0, 7.0, 6.7], [8.6, 7.0, 9.1, 8.7, 9.3]]

print("5 notas dos 3 alunos: \n")
for i in range(3):
    for j in range(5):
        print(turma[i][j], end = " ")
    print("")

print("")

soma_alunos = []
soma = 0

for i in range(3):
    for j in range(5):
        soma += turma[i][j]
    soma_alunos.append(soma)
print(soma_alunos)

media = 0

for notas in soma_alunos:
    media += notas
print("Média total:", (media / 3))
