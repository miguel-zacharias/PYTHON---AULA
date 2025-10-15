numeros = []

for i in range(6):
    n = float(input(f"Digite o {i+1}o número: "))
    numeros.append(n)

soma = sum(numeros)
media = soma / len(numeros)
maior = max(numeros)
menor = min(numeros)

print("Soma:", soma)
print("Média:", media)
print("Maior valor:", maior)
print("Menor valor:", menor)

#feitoporzacharias
