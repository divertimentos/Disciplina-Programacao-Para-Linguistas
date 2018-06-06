turma = {}

while True:
    nome = input("Nome do aluno: \n")
    if (nome == "-1"):
        break
    nota = float(input("Nota do aluno: \n"))
    turma[nome] = nota

maior = 0
melhor = " "

for nome in turma.keys(): # para cada item na lista de chaves,
    if turma[nome] > maior: # se o valor da chave for maior que 'maior'
        maior = turma[nome] # maior é igual o valor da chave
        melhor = nome # melhor é igual à chave
print("Melhor: ", melhor)
