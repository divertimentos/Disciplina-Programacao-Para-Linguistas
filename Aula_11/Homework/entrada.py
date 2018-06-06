lista = []

while True: #Iteração que terminará com um break
    nome = (input("Digite um nome (ou -1 para sair): \n")) #Insere na variável nome o que o usuário digitar.
    if(nome == "-1"): # Se o que o usuário digitar for igual a "-1"
        break #então pare o loop sem fazer nada.
    lista.append(nome) #Caso contrário, pegue o que o usuário digitou e insira na lista
print(lista) #quando o usuário digitar o primeiro -1, tudo o que já estiver inserido na lista será printado.
