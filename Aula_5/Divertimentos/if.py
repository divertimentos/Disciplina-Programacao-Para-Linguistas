sex = input("Insira o sexo: \n")
sex = sex.capitalize()

if sex == "F":
    print("O sexo é feminino.")
elif sex == "M":
    print("O sexo é masculino.")
else:
    if sex != "F" and sex != "M":
        print("Letra não correspondente.")
