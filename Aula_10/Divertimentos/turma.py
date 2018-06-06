turma = {"Ana":3.5, "Pedro": 8.9, "Bianca": 7.8, "Luiz":1.0}

#Chaves:
for nome in turma.keys():
    print("%s é um aluno desta turma." %(nome))

#Valores:
for nota in turma.values():
    print("%2.1f é uma nota desta turma." %(nota))

#Pares
for par in turma.items():
    print(par, "é um aluno-nota desta turma.")
