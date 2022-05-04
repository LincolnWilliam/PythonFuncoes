# Escreva uma função que recebe dois parâmetros e imprime o menor
# dos dois. Se eles forem iguais, imprima que eles são iguais.
def menorNumero (var1,var2):

    if var1 < var2:
         print(f'Entre {var1} e {var2} o menor número é: {var1}')
    elif var1 > var2:
         print(f'Entre {var1} e {var2} o menor numero é:{var2}')
    else:
         print(f'os numeros {var1} e {var2} são iguais.')

var1 = int(input('Informe o primeiro número: '))
var2 = int(input('Informe o segundo número: '))

numero = menorNumero(var1,var2)


#------------ outra maneira de teste direto --------------------
# menorNumero(0,5)
# menorNumero(10,3)
# menorNumero(42,42)