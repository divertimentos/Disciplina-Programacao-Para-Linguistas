turma = {"Ana": 3.5, "Pedro": 8.9, "Bianca": 7.8, "Luiz": 1.0}

print("Ordenados crescentemente por chave:", sorted(turma))

print("Ordenados crescentemente por valor:", sorted(turma, key = turma.get))

print("Ordenados decrescentemente por valor:", sorted(turma, key = turma.get, reverse = True))

#Caramba, que verborrágico esse método de ordenação de dicionário. Mas é bonito.
