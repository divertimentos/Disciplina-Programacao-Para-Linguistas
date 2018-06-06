#Dada uma sentença fornecida pelo usuário, imprimir cada palavra acompanhada de sua frequência de ocorrência na sentença.

sentenca = "nem rei nem lei, nem paz nem guerra, definem com perfil e ser este fulgor baço da terra que é portugal a entristecer. nem fé nem lei, nem mar nem porto. só a prolixa estagnação das mágoas, como nas tardes baças, no mar morto, a dolorosa solidão das águas."

lexico = {}

print("Sentença: %s \n" %(sentenca))

for token in sentenca.split(" "):
    lexico[token] = lexico.get(token, 0) + 1 #Não enteni direito o get e não entendi o que o get fez
for token in sorted(lexico, key = lexico.get, reverse = True):
    print(token, "-", lexico[token])
