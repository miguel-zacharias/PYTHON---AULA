numeros = []

for i in range(10):
    n = int(input(f"Digite o {i+1}o número: "))
    numeros.append(n)

pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("Todos os números:", numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)

#feitoporzacharias
