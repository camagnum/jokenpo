from random import choice
from lib_colors import *

opc_jog = {1:'Pedra',2:'Papel',3:'Tesoura'}
opc_cpu = ['Pedra','Papel','Tesoura']

print(f'''
====================
{colors.ciano}Bem-vindo ao Jokenpô{colors.fim}
====================
''')

while True:
    escolha = int(input('''
    Qual sua escolha?
    [1] Pedra
    [2] Papel
    [3] Tesoura
    '''))

    jogador = opc_jog[escolha]
    print(f'Jogador escolheu {colors.ciano}{jogador}{colors.fim}.')

    computador = choice(opc_cpu)
    print(f'Computador escolheu {colors.ciano}{computador}{colors.fim}.')

    if jogador == computador:
        print(f'{colors.laranja}EMPATE!{colors.fim}')

    elif (jogador == 'Tesoura' and computador == 'Papel') or (jogador == 'Papel' and computador == 'Pedra') or (jogador == 'Pedra' and computador == 'Tesoura'):
        print(f'{colors.verde}O JOGADOR VENCEU!{colors.fim}')

    else:
        print(f'{colors.vermelho}O COMPUTADOR VENCEU!{colors.fim}')