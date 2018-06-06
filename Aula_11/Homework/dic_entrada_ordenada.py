turma = {} #Atribui um dicionário vazio.

while True:
    nome = input("Digite um nome (ou -1 para cancelar): \n")
    if nome == "-1":
        break
    idade = int(input("E sua idade: \n"))
    turma[nome] = idade
print("Turma em ordem crescente pelo nome", sorted(turma))
