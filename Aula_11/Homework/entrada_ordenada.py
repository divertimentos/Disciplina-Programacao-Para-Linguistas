nomes = []

while True:
    nome = input("Digite um nome (ou -1 para sair): \n")
    if nome == "-1":
        break
    nomes.append(nome)
print("Lista ordenada alfabética e crescentemente: %s" %(sorted(nomes))) #sorted ordena por chave. É a ordenação padrão; logo, é a ordenação alfabética crescente.
