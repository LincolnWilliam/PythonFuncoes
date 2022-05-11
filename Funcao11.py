# Calculadora simples com as 4 operações.
def calc ():

        if tipo == '1':
            soma = a + b
            print (f'a soma dos números informados é: {soma}')

        elif tipo == '2':
            subtracao = a - b
            print(f'a subtração dos números informados é: {subtracao}')

        elif tipo == '3':
            try:
                divisao = a / b
                print(f'a divisão dos números informados é: {divisao}')
            except ZeroDivisionError:
                print('zero não é divisor. ')

        elif tipo == '4':
            multiplicacao = a * b
            print(f'a multiplicação dos números informados é: {multiplicacao}')


a = int(input('informe o primeiro número: '))
b = int(input('informe o segundo número: '))
tipo = input('1-soma\n'
             '2-subtração\n'
             '3-divisão\n'
             '4-multiplicação\n'
             'informe o codigo do tipo de calculo: ')
calc()