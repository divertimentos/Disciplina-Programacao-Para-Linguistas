menor = int(input("Digite um inteiro positivo inicial: \n"))
maior = int(input("Digite um inteiro positivo final: \n"))
primos = 0

while menor < 0 or maior < 0:
    menor = int(input("Digite um inteiro positivo inicial: \n"))
    maior = int(input("Digite um inteiro positivo final: \n"))
else:
    for num in range(menor, maior + 1):
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num)
                primos += 1

    print("A quantidade de primos é: %d." %(primos))
