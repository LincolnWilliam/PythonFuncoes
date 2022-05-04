# Programinha mostra se o número é positivo ou negativo
# veja README.md

def positivo_negativo(n):

        if n == 0:
            print(f'{n}(zero)é um numero neutro, informe outro número')

        elif n > 0:
            print(f'{n} é um número positivo.')

        else:
            print(f'{n} é um número negativo.')

n = int(input("Informe o número: "))
numero = positivo_negativo(n)
