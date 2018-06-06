idade = {"Ana": 3, "Pedro": 18, "João": 6}

print(idade.get("Ana"))
print(idade.get("Gui", "Valor secundário."))

idade["Gui"] = 24

print(idade.get("Guilherme"))
