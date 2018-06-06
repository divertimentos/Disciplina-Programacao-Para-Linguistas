nomes = []
notas = []

for i in range(3):
    nomes.append(input("Nome do aluno: \n"))
    notas.append(float(input("Nota do aluno %s: \n" %(nomes[i]))))

media = ((notas[0] + notas[1] + notas[2]) / 3)

for j in range(3):
    if notas[j] > media:
        print("Parabéns, %s, sua nota está acima da média." %(nomes[j]))
