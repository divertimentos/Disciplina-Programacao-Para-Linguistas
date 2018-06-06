#Cálculo de média de notas de uma turma com 10 alunos.

notas = [10, 9, 7, 5, 6, 7, 8, 2, 9, 4]
índice = (len(notas))
total = sum(notas)
media = total / índice
media = round(media, 1)

print("\nA lista de notas é: %s" %notas)
print("O índice de notas é: %s" %índice)
print("A média das notas é: %s." %media)

#Eu fiz diferente da Helena. Calcular média é mais fácil usando for.
