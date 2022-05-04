# Retornar FzzBuzz , Fizz , Buzz
# ver README.md
def FizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')

    elif n % 3 == 0:
        print('Fizz')

    elif n % 5 == 0:
        print('Buzz')

    else:
        return n

resultado = FizzBuzz(int(input('Informe um número: ')))
print(resultado)
