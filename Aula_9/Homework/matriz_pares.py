# n == linha
# m == coluna

n = int(input("Quantas linhas? \n")) #Variável linha
m = int(input("Quantas colunas? \n")) #Variável coluna

matriz = [] #Variável que receberá as linhas contendo os vetores
pares = 0 #Variável que será o contador de pares na iteração final

for i in range(n): #Para cada i(linha) que o usuário pediu, crie uma linha.
    linha = []
    for j in range(m):
        linha.append(int(input("Digite um valor: \n")))
    matriz.append(linha)

for i in range(n):
    for j in range(m):
        if (matriz[i][j] % 2 == 0):
            pares += 1
print("Quantidade de pares é: %d." %(pares))
