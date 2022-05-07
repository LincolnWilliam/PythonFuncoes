# Escrevendo em número ordinal e cardinal o número digitado
#Ler README.md
from num2words import num2words

def OrdinalCardinal():

        num_en = num2words(numero, lang= 'en')
        print(f'Em inglês: {num_en}')

        num_en_ord = num2words(numero, lang= 'en', to='ordinal')
        print(f'Em inglês (ordinal): {num_en_ord}')

        num_pt = num2words(numero, lang= 'pt-br')
        print(f'Em Português: {num_pt}')

        num_pt_ord = num2words(numero, lang='pt-br', to='ordinal')
        print(f'Em Português (Ordinal): {num_pt_ord}')


numero = int(input('Informe um número: '))

OrdinalCardinal()