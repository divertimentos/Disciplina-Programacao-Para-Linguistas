notas = open("notas.txt", "r", encoding="utf-8")
medias = open("medias.txt", "w", encoding="utf-8")

for aluno in notas:
    (aluno, nota1, nota2, nota3) = aluno.split(" ")
    media = (float(nota1) + float(nota2) + float(nota3)) / 3
    medias.write(aluno + " " + "%.2f" % media + "\n")

notas.close()
medias.close()
