num = -1

while (num < 0):
    num = int(input("Digite um número inteiro: \n"))
    for i in range(0, num + 1):
        if (i % 2 == 0):
            print(i)
