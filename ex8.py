#feito por Miguel Zacharias
# Exercício 8 — Combinação de Operadores Lógicos e Relacionais
x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
z = int(input("Digite o valor de z: "))

print(f"x > y and y > z: {x > y and y > z}")
print(f"x > y or y > z: {x > y or y > z}")
print(f"x == y or x == z: {x == y or x == z}")
print(f"x != y and y != z: {x != y and y != z}")
print(f"not (x > y) and z > y: {not (x > y) and z > y}")
print(f"(x > y and y > z) or (x == z): {(x > y and y > z) or (x == z)}")
