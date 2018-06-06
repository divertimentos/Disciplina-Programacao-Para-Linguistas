nomes = []
notas = []
n = 0
maior = 0

while n != -1:
    nomes.insert(0, input("Digite um nome (Digite -1 para encerrar o programa)): \n")) #Pedido 1/2
    if (nomes[0] == "-1"):
        break
    else:
        notas.insert(0, float(input("Digite uma nota: \n"))) #Pedido 2/2
        n = notas[0]
        if (n > maior):
            maior = n
        else:
            break
print("Resultado: \n\nA maior nota foi de %s. Sua nota foi: %1.1f." %(nomes[1], maior))

#Consegui. Claro que no futuro poderei melhorar esse algoritmo; mas eu consegui fazer rodar certinho.
