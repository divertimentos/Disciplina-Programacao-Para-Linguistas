sentenca = "A cada dia que passa, a sombra da manhã do dia fica mais linda, como se o dia lindo fosse cada dia mais lindo a cada sombra que passasse."

tokens = sentenca.split(" ") # Ordenação
lexico = {} #Inicializa o dicionário

for token in tokens:
    lexico[token] = lexico.get(token, 0) + 1
for token in sorted(lexico.keys(), key = lexico.get, reverse = True):
    print(token, "-->", lexico[token]/len(tokens))
