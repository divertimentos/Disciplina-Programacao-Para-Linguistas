string = ("cadeado")
substring = ("de")

posicao = string.find(substring)
print(string[0: posicao], end = "")
print(string[posicao:posicao+len(substring)].upper(), end = "") #Falta entender essa linha.
print(string[posicao + len(substring): len(string)]) #Esta linha eu entendi.
