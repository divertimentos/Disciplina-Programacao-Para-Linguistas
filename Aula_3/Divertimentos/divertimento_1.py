while True:
    nota = input( " \nNota: \n")
    nota = float(nota)

    # De 0.0 até 1.0 o conceito é F.
    # De 1.1 até 2.0 o conceito é E.
    # De 2.1 até 4.0 o conceito é D.
    # De 4.1 até 7.0 o conceito é C.
    # De 7.1 até 9.0 o conceito é B.
    # De 9.1 até o infinito o conceito é A.

    #Preciso fazer a nota máxima ser 10.

    if nota <= 1.0:
        print ("Sua nota foi %s, então seu conceito é F." %nota)
    elif nota <= 2.0:
        print ("Sua nota foi %s, então seu conceito é E." %nota)
    elif nota <= 4.0:
        print ("Sua nota foi %s, então seu conceito é D." %nota)
    elif nota <= 7.0:
        print("Sua nota foi %s, então seu conceito é C." %nota)
    elif nota <= 9:
        print("Sua nota foi %s, então seu conceito é B." %nota)
    elif nota <= 10:
        print("Sua nota foi %s, então seu conceito é A." %nota)
    else:
        print("A nota %s está fora do conceito. Tente novamente." %nota)

    # if nota > 10.0:
    #    print("A nota %s está fora do conceito. Tente novamente!" %nota)
