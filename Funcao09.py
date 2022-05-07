# Sortear número no intervalo de 2 números informados.

import random

def sorteado():
    return random.randrange(a, b, 1)
a = int(input('Informe o primeiro número: '))
b = int(input('informe o segundo número: '))

print(f'Número sorteado entre {a} e {b} vai ser: ', sorteado())
