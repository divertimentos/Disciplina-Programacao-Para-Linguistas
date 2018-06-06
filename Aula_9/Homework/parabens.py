#Exercício 6

matriz = []
soma = 0

for i in range(3):
    linha = []
    for j in range(1):
        linha.append(input("Nome do aluno: \n")) #Insere a string no vetor
        linha.append(float(input("Nota: \n"))) #Insere o float no vetor, após a string
    matriz.append(linha) #Insere a linha preenchida na matriz ao final de cada iteração

for i in range(3):
    soma += matriz[i][1] #soma das notas
media = (soma / 3)

print("A média de notas é: %2.1f." %(media))

for i in range(3):
    if (matriz[i][1] > media): #Se os itens da coluna das notas forem maiores que a média, imprima o respectivo nome em cada iteração.
        print("Parabéns, %s." %(matriz[i][0]).capitalize())

# Consegui! Só não fiz do jeito que a Helena fez.
