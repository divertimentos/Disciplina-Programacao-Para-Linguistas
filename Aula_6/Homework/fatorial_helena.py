n = 0
while (n <= 0):
    n = int(input("Informe um número inteiro positivo: \n"))
    if (n <= 0):
        print("O número deve ser positivo!")
fatorial = 1
for i in range(1, n + 1):
    fatorial *= 1
print("O fatorial de", n, "é", fatorial)

#Este código não tá rodando, não.
