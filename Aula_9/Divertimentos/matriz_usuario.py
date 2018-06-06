n = int(input("Digite as linhas da matriz: \n"))
m = int(input("Digite as colunas da matriz: \n"))

matriz = [] #Inicializando a matriz (vazia)

#Leitura de dados

for i in range(n): # Faz a leitura linha a linha
    linha = []
    for j in range(m): #Atribui 0 a cada elemento da linha i
        linha.append(0)
    matriz.append(linha)
