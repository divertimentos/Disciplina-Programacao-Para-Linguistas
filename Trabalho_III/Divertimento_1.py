# Faça um programa que:

# (1) peça ao usuário vários números inteiros positivos (até que ele digite -1 para sair),

# (2) imprima esses números ordenados crescentemente.

# Utilize uma estrutura de dados (lista, matriz ou dicionário) para armazenar os números.

lista = [] #Inicia uma lista vazia chamada lista.

# Pedido de números inteiros positivos e teste como condição de parada do while:
while True: # Laço que só será terminado por um break
    entrada = int(input("Digite um número (ou -1 para sair): \n")) #Usuário entra um inteiro
    if(entrada == -1): # Se a entrada do usuário for igual a -1,
        break # Pare o laço e vá para a identação exterior
    lista.append(entrada) # A cada laço, insira o valor de "entrada" na lista

#Print dos números ordenados crescentemente:

print(sorted(lista)) #Após o break e a inserção dos valores à lista, printe a lista de números crescentemente.
