#feitoporzacharias
qtd = int(input('Quantas notas você vai informar? '))
soma = 0
for i in range(1, qtd+1):
    nota = float(input(f'Digite a nota {i}: '))
    soma += nota
media = soma / qtd
print(f'Média: {media:.1f}')
if media >= 7:
    print('Situação: Aprovado')
elif media >= 5:
    print('Situação: Recuperação')
else:
    print('Situação: Reprovado')