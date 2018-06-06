#Exibição de todos os números pares entre 0 e um valor(número inteiro) indicado pelo usuário.

numero = int(input("Digite um número: \n"))

for i in range(0, numero + 1):
    if i % 2 == 0:
        print(i)

if numero % 2 != 0:
    print("Ímpar")
