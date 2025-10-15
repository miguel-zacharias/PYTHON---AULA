#feito por Miguel Zacharias
# Exercício 7 — Operador Lógico NOT
A = input("Digite o valor de A (True/False): ") == "True"
B = input("Digite o valor de B (True/False): ") == "True"
C = input("Digite o valor de C (True/False): ") == "True"

print(f"not A: {not A}")
print(f"not B: {not B}")
print(f"not C: {not C}")
print(f"not (A and B): {not (A and B)}")
print(f"not (A or B): {not (A or B)}")
print(f"not A and not B: {not A and not B}")
print(f"not (not A): {not (not A)}")
