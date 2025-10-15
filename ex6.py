#feitoporzacharias
n = int(input('Digite um número: '))
primo = True
if n < 2:
    primo = False
else:
    for i in range(2, n):
        if n % i == 0:
            primo = False
            break
if primo:
    print(f'O número {n} é primo.')
else:
    print(f'O número {n} não é primo.')