entrada = "a cada lindo dia, a linda árvore fica, no dia a dia, cada vez mais linda."
lexico = {}
tokens = entrada.split(" ")

for token in tokens:
    lexico[token] = lexico.get(token, 0) + 1 #Tô entendendo melhor o get

for token in lexico.keys():
    lexico[token] = lexico.get(token) / len(tokens)



while True:
    token = input("Forneça um token (ou digite -1 para sair): \n")
    if token == "-1":
        break
    print(token, "-->", lexico.get(token, 0))
