nome = senha = " "

while senha == nome:
    nome = input("Digite seu nome: \n")
    senha = input("Digite sua senha: \n")
    if senha == nome:
        print("Erro: O usuário e a senha são idênticos, tente novamente.")
print("Login efetuado com sucesso.")
