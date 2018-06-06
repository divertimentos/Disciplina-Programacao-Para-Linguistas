sentenca = "Só o mar das outras que é belo. Aquele que nós vemos dá-nos sempre saudades daquele que não veremos nunca. A cada dia o dia parece ser o dia mais bonito do que aquele dia bonito que não veremos nunca, segundo Fernando Pessoa."
sentenca = sentenca.lower()
tokens = {}

for token in sentenca.split(" "): # Para cada token na sentença splitada por espaço,
    tokens[token] = tokens.get(token, 0) + 1 # Dentro do dicionário tokens, adicione à chave 'token' o valor: Busque os token dentro do dicionário de tokens. Se não houver, chame-o de o (zero) e adicione 1. Se token for diferente de 0 (zero) some 1 do mesmo jeito.
for token in (sorted(tokens)): #Para cada item no dicionário de tokens
    print(token, "-", tokens[token]) #Printe a chave, depois printe "-", depois printe o valor dessa chave.
