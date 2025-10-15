nomes = []

for i in range(5):
    nome = input(f"Digite o {i+1}o nome: ")
    nomes.append(nome)

busc = input("Digite um nome para buscar: ")

if busc in nomes:
    print(f'O nome "{busc}" está na lista.')
else:
    print(f'O nome "{busc}" não está na lista.')

#feitoporzacharias
