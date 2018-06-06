entrada = open('teste_pt.txt', 'r', encoding = 'utf-8')
saida = open('saida.txt', 'w', encoding = 'utf-8')

for linha in entrada:
    saida.write(linha)

entrada.close()
saida.close()
