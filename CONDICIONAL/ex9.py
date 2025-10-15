# Exercício 9 — Categoria de Idade
idade = int(input('Digite a idade: '))
if idade < 12:
    categoria = 'Criança'
elif idade < 18:
    categoria = 'Adolescente'
elif idade < 60:
    categoria = 'Adulto'
else:
    categoria = 'Idoso'
print(f'Categoria: {categoria}')
