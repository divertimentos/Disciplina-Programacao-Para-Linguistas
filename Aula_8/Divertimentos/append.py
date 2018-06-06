notas = []
for i in range(2): #Comando de repetição para que o programa peça 2 notas.
    n = float(input("Digite uma nota: \n"))
    notas.append(n) #Inserção.
print(notas)

notas.insert(1, (notas[0] + notas[1]) / 2) #inserção com acesso dos elementos.
print(notas)
