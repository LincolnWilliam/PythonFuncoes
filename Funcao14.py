# Atividade - Controle Remoto
# Ler README.md Funcao14
canal = 1
volume = 18

def mudarCanal():
    global canal

    if canal == 1:
        canal = 2
        print('Você está assistindo Jornal Record')
    elif canal == 2:
        canal = 3
        print('Você está assistindo Jornal Band !')
    else:
        canal = 1
        print('Você está assistindo programa do Silvio Santos')


def aumentarVolume():
    global volume
    if volume == 20:
        print('Volume muito alto,pode causar perda irreversível da audição!!')
    else:
        volume +=1
        print(f'Volume da TV: {volume}')


def diminuirVolume():
    global volume
    if volume == 0:
        print('Volume no minimo ')
    else:
        volume -=1
        print(f'Volume da TV: {volume}')


while True:

    opcao = int(input('Escolha uma opção\n'
                    '1 - Alterar Canal\n'
                    '2 - Aumentar volume\n'
                    '3 - Diminuir volume\n'
                    '4 - Desligar a TV\n'
                    'Selecione uma opção: '))

    if opcao == 1:
        mudarCanal()

    elif opcao == 2:
        aumentarVolume()

    elif opcao == 3:
        diminuirVolume()

    elif opcao == 4:
        print('Desligando...')
        break
    else:
        print('Opção inválida')