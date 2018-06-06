
contagem = input("Digite um valor menor ou igual a 10:\n")
contagem = float(contagem)

while contagem > 0 and contagem < 10.1:
    contagem = contagem - 1
    print(contagem)

if contagem >= 10.1:
    print("ERRO! Digite um número menor ou igual a 10!")
