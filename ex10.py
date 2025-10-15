#feitoporzacharias
import random
print('Tente adivinhar o número entre 1 e 50!')
segredo = random.randint(1, 50)
while True:
    palpite = int(input('Digite seu palpite: '))
    if palpite > segredo:
        print('Muito alto! Tente novamente.')
    elif palpite < segredo:
        print('Muito baixo! Tente novamente.')
    else:
        print('Parabéns! Você acertou!')
        break