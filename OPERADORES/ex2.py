#feito por Miguel Zacharias
# Solicita dois números inteiros
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Calcula os resultados
div_real = num1 / num2
div_int = num1 // num2
dif = div_real - div_int

# Exibe os resultados
print(f"Divisão real: {div_real}")
print(f"Divisão inteira: {div_int}")
print(f"Diferença: {dif}")
