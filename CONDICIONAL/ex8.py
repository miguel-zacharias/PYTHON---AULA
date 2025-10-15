# Exercício 8 — Calculadora Simples com Condicionais
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
op = input('Digite o operador (+, -, *, /): ')
if op == '+':
    resultado = num1 + num2
elif op == '-':
    resultado = num1 - num2
elif op == '*':
    resultado = num1 * num2
elif op == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = 'Erro: divisão por zero'
else:
    resultado = 'Operador inválido'
print(f'Resultado: {resultado}')
