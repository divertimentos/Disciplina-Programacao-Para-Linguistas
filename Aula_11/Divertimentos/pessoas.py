pessoas  = {}

while True:
    nome = input("Digite um nome: \n")
    if nome == "-1":
        break
    idade = float(input("Idade: \n"))
    pessoas[nome] = idade
    ordenado = sorted(pessoas, key = pessoas.get)
    print(ordenado)
