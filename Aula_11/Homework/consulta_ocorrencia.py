sentenca = "a cada dia que passa o dia que passa fica mais lindo que o lindo dia anterior que sempre passa por causa da natureza de cada dia que passa."
tokens = sentenca.split(" ")
lexico = {}
for token in tokens:
    lexico[token] = lexico.get(token, 0) + 1
while True:
    token = input("Forneça um token para consulta (-1 para sair): \n")
    if (token == "-1"):
        break
    print(token, "tem uma probabilidade de:", lexico.get(token, 0) / len(tokens))
