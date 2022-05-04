# Retornar 1 ou 2 , de acordo com os casos,
# ver README.md
def maiorLimite(a, b, limite):

    if a > limite and b > limite:
        return 2

    elif a > limite or b > limite:
        return 1

    else:
        return 0

a = int(input('Informe um número:'))
b = int(input('Informe um número:'))
limite = int(input('Informe um número:'))

resultado = maiorLimite(a,b,limite)
print(resultado)
