# Escreva uma função que irá calcular a área de um retângulo,
# a mesma irá precisar dos valores da base e da altura como
# parâmetros para poder calcular a área.
# (área = base * altura / 2)

def areaRetangulo(base,altura):

    return (base * altura) / 2

base = int(input('infomre a base do retângulo: '))
altura = int(input('infomre a Altura do retângulo: '))
area = areaRetangulo(base,altura)

print(f'O retangulo de base:{base} e altura:{altura} tem uma área de: {area}')

