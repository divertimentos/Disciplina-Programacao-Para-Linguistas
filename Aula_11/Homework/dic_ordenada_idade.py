turma = {}

while True:
    nome = input("Digite um nome (ou -1): \n")
    if nome == "-1":
        break
    turma[nome] = int(input("E sua idade: \n"))
print("Turma ordenada pela idade:", sorted(turma, key = turma.get))

# Ainda preciso entender certinho como funciona  o get() e os parâmetros do sorted()
