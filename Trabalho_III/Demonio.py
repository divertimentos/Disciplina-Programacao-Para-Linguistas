# Faça um programa que:

# (1) peça ao usuário um número inteiro positivo (n) referente às dimensões de uma matriz quadrada n x n,

# (2) leia os n*n números inteiros que compõem as n linhas e as n colunas dessa matriz

# (3) imprima a SOMA dos números na diagonal principal. Utilize uma estrutura de dados (matriz) para armazenar os dados fornecidos pelo usuário.

matriz = []
n = int(input("Digite o tamanho da matriz: \n"))
zero = 0

for i in range(1, n + 1): # Para cada i(variável interna) dentro do range que vai de 0 até 'o número que designa o tamanho da matriz + 1',
    linhas = [] #crie um vetor vazio chamado 'linhas'
    matriz.append(linhas) # e adicione o vetor criado ao vetor matriz, criando um vetor composto por vetor (matriz)
    for j in range(1, n + 1): #para cada j(variável interna que servirá como coluna) dentro do mesmo range do for exterior,
        if(i != j): # Se o índice de i e j não forem iguais
            linhas.append(zero) # Adicione um valor vazio à celula
        elif(i == j): # Se/quando houver uma coordenada onde o número da linha e o número da coluna são iguais,
            soma = i + j # Então atualize a variável soma para a soma de linha + coluna e
            linhas.append(soma) #Adicione o valor da variável soma à célula, em vez de zero.

#Printa a matriz, linha por linha, com as somas dos números na diagonal principal, não importa seu tamanho.
for i in matriz: #Para cada linha na matriz,
    print(i) # Printe cada linha da matriz.
