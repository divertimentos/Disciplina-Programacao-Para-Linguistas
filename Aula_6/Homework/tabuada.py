entrada = int(input("Tabuada: \n"))
indice = -1

while indice <= 9:
    indice = indice + 1
    tabuada = entrada * indice
    print( entrada, "x", indice, "=", tabuada)
