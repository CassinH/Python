from time import sleep
from random import randint
lista =list()
jogos = list()
print('_'*30)
print('   JOGA NA MEGA SENA     ')
print('_'*30)
quant= int(input('Quantos jogos você quer que sorteie? '))
tot =1
while tot <=quant:
    cont=0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont>=6:
            break
        lista.sort()
        jogos.append(lista[:])
        tot +=1
        print('_' * 30,f'SORTEANDO {quant}JOGOS','_'*30)
        for i,l in enumerate(jogos):
            print(f'Jogo {i+1}: {l}')
            sleep(1)
        print('-='*6, '< BOA SORTE! >','-='*6)
            