turma = []
# Leitura das notas
while True: #Leitura de nomes e notas
    nome = input("Nome: \n")
    if nome == "'-1"':
        break
    nota = float(input("Nota: \n"))
    turma.append([nome, nota])
if len(turma) > 0: #Se alguma nota foi digitada
    maior = turma[0][1] #Considera como maior nota a primeira nota
    melhor = turma[0][0] # Considera o melhor aluno o primeiro
    for aluno in turma: #Verifica se há aluno melhor que ele
        if aluno[1] > maior: #Se sim,
            maior = aluno[1] #Atualiza a melhor nota
            melhor = aluno[0] #Atualiza o nome do aluno cuja nota é a maior
    print("O melhor aluno é:",melhor) #Printa ao final de cada iteração
