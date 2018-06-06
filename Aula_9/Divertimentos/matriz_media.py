turma = [[1, 2, 3, 4, 5], [5, 6, 5, 6, 4], [10, 9, 10, 8, 9]]
media = 0

for i in range(3):
    for j in range(5):
        media += turma[i][j]
print(media / 15)
