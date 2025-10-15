#feitoporzacharias
pares = 0
impares = 0
soma = 0
for i in range(1, 11):
    num = int(input(f'Digite o {i}o número: '))
    soma += num
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')
print(f'Soma total: {soma}')