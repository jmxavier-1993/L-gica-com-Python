x = int(input("Digite um número inteiro X: "))

for n in range(1, 6):
    potencia = x ** n
    if potencia > 100:
        print(f"O valor {x}^{n} é alto")
    else:
        print(potencia)