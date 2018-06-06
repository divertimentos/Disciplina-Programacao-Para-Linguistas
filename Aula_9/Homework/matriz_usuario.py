n = int(input("Quantas linhas? \n"))
m = int(input("Quantas colunas? \n"))
matriz = [] #Inicializando a matriz vazia.

#Leitura de dados

for i in range(n): #Faz a leitura linha a linha
    linha = []
    for j in range(m): #Atribui 0 a cada elemento da linha i
        linha.append(0)
    matriz.append(linha) #Adiciona uma linha na matriz para cada iteração

for i in range(n):
    print(matriz[i])
