entrada = int(input("Digite um número e descubra seu fatorial: \n"))
contador = entrada

while contador > 1:
    contador = (contador - 1)
    entrada = (entrada * contador)
print("O fatorial do número digitado é: %s" %entrada)
