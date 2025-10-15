# Exercício 6 — Verificação de Triângulo
a = float(input('Digite o primeiro lado: '))
b = float(input('Digite o segundo lado: '))
c = float(input('Digite o terceiro lado: '))
if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        tipo = 'equilátero'
    elif a == b or a == c or b == c:
        tipo = 'isósceles'
    else:
        tipo = 'escaleno'
    print(f'Os lados formam um triângulo {tipo}.')
else:
    print('Os lados não formam um triângulo.')
