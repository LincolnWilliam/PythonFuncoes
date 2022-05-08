# soma dos n primeiros inteiros positivos
numero = int(input('informe um numero interiro:'))
soma = 0
i = 1

while i <= numero:
    soma = soma + i
    i += 1
print (soma)