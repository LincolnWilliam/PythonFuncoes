# Escreva uma função que recebe dois parâmetros e imprime o menor
# dos dois. Se eles forem iguais, imprima que eles são iguais.
def menorNumero (var1,var2):
     if var1 < var2:
         print(f'menor numero é: {var1}')
     elif var1 > var2:
         print(f'menor numero é:{var2}')
     else:
         print('os numeros sao iguais.')

#------------ outra maneira de teste direto --------------------
menorN(0,5)
menorN(10,3)
menorN(42,42)