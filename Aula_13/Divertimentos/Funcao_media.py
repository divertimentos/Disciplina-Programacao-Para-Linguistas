# Abre o arquivo utf-8 para leitura:
arqnotas = open("notas.txt", "r", encoding = "utf-8")
# Abre o arquivo utf-8 para escrita:
arqmedias = open("medias.txt", "w", encoding = "utf-8")

#Lê o conteúdo do arquivo de entrada, calcula a média de cada aluno e imprime o resultado no arquivo de saída
for aluno in arqnotas: # para cada aluno
    (nome, nota1, nota2, nota3) = aluno.split(" ")
    media = (float(nota1) + float(nota2) + float(nota3)) / 3
    arqmedias.write(nome + " %1.2f" %media + "\n")

#Fecha os arquivos previamente abertos
arqnotas.close()
arqmedias.close()
