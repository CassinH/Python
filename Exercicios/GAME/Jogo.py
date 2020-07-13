from random import randint
itens =('Pedra','Papel, Tesoura')
computador = randint(0,2)
print('''Sua Opções:
[0] PEDRA
[1} PAPEL
[2] TESOURA''')
jogador=int(input('Qual é a sua jogada? '))
print('-=' *12)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}' .format(itens[jogador]))
print('-='*12)
if computador == 0: #PEDRA
    if jogador==0:
        print('EMPATE')
    elif jogador==1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA! ')
if computador == 1: #PAPEL
    if jogador==0:
        print('EMPATE')
    elif jogador==1:
        print('JOGADOR VENCEU')
    elif jogador ==2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA! ')
if computador == 2: # PAPEL
            if jogador == 0:
                print('EMPATE')
            elif jogador == 1:
                print('JOGADOR VENCEU')
            elif jogador==2:
                print('COMPUTADOR VENCE')
            else:
                print('JOGADA INVÁLIDA! ')
