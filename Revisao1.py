soma_pares = 0
n = int(input("Digite um número: "))
for i in range(2, n, 2):
    soma_pares += i

print(f"A soma dos números pares até {n} é: {soma_pares}")

if soma_pares > 100:
    print("A soma é alta!")
else:
    print("A soma é baixa!")