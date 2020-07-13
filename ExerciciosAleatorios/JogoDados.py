from random import randint
from time import sleep
from operator import itemgetter
jogo={'Cassio':randint(1,6),
      'Maria': randint(1,6),
      'Gustavo':randint(1,6),
      'Natha':randint(1,6),
      'João':randint(1,6)}
ranking=list()
print('VALORES SORTEADOS:')
for k,v in jogo.items():
    print(f'{k}tirou {v} no dado.')
    sleep(1)
    ranking=sorted(jogo.items(),key=itemgetter(1),reverse=True)
    print('-='*35)
    print('==RANKING DOS JOGADORES ==')
    for i,v in enumerate(ranking):
        print(f'{i+1}º luga: {v[0]} com {v[1]}.')
        sleep(1)