# Função radar de velocidade
# Parâmetros (velocidade do veiculo, limite de velocidade, placa)
# Ler README.md
def radar (velocidade, limite, placa):

    if velocidade > limite3:
        print(f'Veiculo da placa {placa} foi multado em R$ 989,00')
    elif velocidade > limite2:
        print(f'Veiculo da placa {placa} foi multado em R$ 400,00')
    elif velocidade > limite1:
        print(f'Veiculo da placa {placa} foi multado em R$ 189,00')
    else:
        print(f'Veiculo dentro da velocidade!!')

velocidade = int(input('informe a velociade do veiculo:'))
limite = int(input('informe o limite de velocidade:'))
placa = int(input('informe a placa do veiculo:'))
limite1 = (velocidade * 20) / 100 + limite
limite2 = (velocidade * 50) / 100 + limite
limite3 = (velocidade * 80) / 100 + limite

radar (velocidade, limite, placa)

#  mesmo resultado:

# def radar (velocidade, limite, placa):
#     if velocidade > (limite * 0.2) + limite and velocidade < (limite * 0.5) + limite:
#         print(f'Veiculo da placa {placa} foi multado em R$ 189,00')
#     elif velocidade > (limite * 0.5) + limite and velocidade < (limite * 0.8) + limite:
#         print(f'Veiculo da placa {placa} foi multado em R$ 400,00')
#     elif velocidade > (limite * 0.8) + limite:
#         print(f'Veiculo da placa {placa} foi multado em R$ 989,00')
#     else:
#         print(f'Veiculo dentro da velocidade!!')
#
# radar(100,50,'acb-1298')