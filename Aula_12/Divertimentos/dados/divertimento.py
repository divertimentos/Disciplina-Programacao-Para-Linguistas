dados = open("dados.txt", "w", encoding="utf-8")

while True:
    nome = input("Digite um nome (ou digite -1): \n")
    if nome == "-1":
        break
    idade = input("Digite uma idade: \n")
    dados.write(nome + " " + idade + "\n")
dados.close()
