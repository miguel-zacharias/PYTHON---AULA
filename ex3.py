#feito por Miguel Zacharias
# Exercício 3 — Operador Módulo (%)
num = int(input("Digite um número: "))

resto2 = num % 2
resto3 = num % 3
resto5 = num % 5
resto10 = num % 10

par_ou_impar = "par" if resto2 == 0 else "ímpar"

print(f"Resto por 2: {resto2} (Número {par_ou_impar})")
print(f"Resto por 3: {resto3}")
print(f"Resto por 5: {resto5}")
print(f"Resto por 10: {resto10}")
