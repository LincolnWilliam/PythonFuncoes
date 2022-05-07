# Crie uma função que receba  2 números.
# O primeiro é um valor e o segundo um percentual (ex. 10%).
# Retorne o valor do primeiro número somado do aumento do percentual do mesmo.
# resumo :
# calcular o aumento de salário.

def aumento_salario(a,b):
    return a + (a * b / 100)

a = float(input('Informe um valor atual do salário: R$ '))
b = float(input('Informe o aumento: % '))

i = aumento_salario(a,b)
print(f'seu salário subiu de R$ {a} para R$ {i:.2f}')

