# Exercício 10 — Precedência de Operadores
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

print(f"a + b * c = {a + b * c} (Multiplicação antes da soma)")
print(f"(a + b) * c = {(a + b) * c} (Parênteses antes da multiplicação)")
print(f"a ** b + c = {a ** b + c} (Exponenciação antes da soma)")
print(f"a ** (b + c) = {a ** (b + c)} (Parênteses antes da exponenciação)")
print(f"a + b / c = {a + b / c} (Divisão antes da soma)")
print(f"(a + b) / c = {(a + b) / c} (Parênteses antes da divisão)")
print(f"a % b + c * 2 = {a % b + c * 2} (Multiplicação antes da soma, resto antes da soma)")
print(f"(a + b * c) ** 2 - a = {(a + b * c) ** 2 - a} (Multiplicação antes da soma, depois exponenciação, depois subtração)")
