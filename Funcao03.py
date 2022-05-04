def somaMaiorLimite(a,b,limite):
    soma = a + b
    if soma > limite:
        return True
    else:
        return False
a = int(input('Informe o primeiro número: '))
b = int(input('Informe o segundo número: '))
limite = int(input('Informe o terceiro número: '))

i = somaMaiorLimite(a,b,limite)
print(i)