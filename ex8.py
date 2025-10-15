#feitoporzacharias
maior = None
menor = None
for i in range(1, 6):
    num = int(input(f'Digite o {i}o número: '))
    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')