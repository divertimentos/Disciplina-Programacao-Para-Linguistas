# Faça um programa que:

# (1) peça ao usuário vários nomes e respectivas idades (até que ele digite -1 para sair),
# (2) imprima todos os nomes acompanhados da idade, ordenados crescentemente pelo nome da pessoa.

#Utilize uma estrutura de dados (lista, matriz ou dicionário) para armazenar os dados (nome e idade) de cada pessoa.


turma = {} # Cria um dicionário vazio chamado turma.

while True: # Enquanto não houver uma condição de parada:
    nome = input("Digite um nome (ou -1 para sair): \n") # Pedido de string ao usuário, armazenada na variável nome.
    if(nome == "-1"): # Se nome for igual à string -1,
        break # Sai do laço.
    idade = int(input("Digite a idade: \n")) # Caso não, pede um valor e o adiciona à variável idade
    turma[nome] = idade # Adiciona ao dicionário o valor de "idade" atribuído à chave "nome", dados na mesma iteração.

for nome in sorted(turma): #Para cada chave presente no dicionário "turma", ordenado alfabeticamente,
    print(nome,"-", turma[nome]) #Imprima a chave e seu respectivo valor
