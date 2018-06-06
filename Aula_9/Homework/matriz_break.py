#Exercício 7

matriz = []
maior = 0

while True:
    for i in range(1):
        lista = []
        lista.append(input("Nome: \n"))
    if lista[0] == "-1":
        break
    else:
        lista.append(float(input("Nota: \n")))
        matriz.append(lista)
        contador = lista[1]
if contador > maior:
    maior = contador
print("A maior nota é:", contador)

#Consegui, só que tá diferente do da Helena, pois o dela printa printa o maior a cada iteração.
