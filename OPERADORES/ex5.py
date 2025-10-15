#feito por Miguel Zacharias
# Exercício 5 — Operador Lógico AND
A = input("Digite o valor de A (True/False): ") == "True"
B = input("Digite o valor de B (True/False): ") == "True"
C = input("Digite o valor de C (True/False): ") == "True"
D = input("Digite o valor de D (True/False): ") == "True"

print(f"A and B: {A and B}")
print(f"C and D: {C and D}")
print(f"A and B and C: {A and B and C}")
print(f"A and B and C and D: {A and B and C and D}")
print(f"(A and B) and (C and D): {(A and B) and (C and D)}")
