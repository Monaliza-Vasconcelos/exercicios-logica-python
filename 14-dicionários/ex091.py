from random import randint
from time import sleep
import os
from operator import itemgetter
os.system('cls')
game = {'jogador1':randint(1,6),
        'jogador2':randint(1,6),
        'jogador3':randint(1,6),
        'jogador4':randint(1,6)}
ranking = list()
print(f'Valores sorteados: ')
for k,v in game.items():
    print(f'O {k} tirou {v}')
    sleep(0.5)
ranking = sorted(game.items(), key=itemgetter(1), reverse=True) #O 1 é para colocar em ordem de chave
print('-'*30)
print('Ranking dos jogadores: ')
for i, v in enumerate(ranking,start=1):
    print(f'{i} lugar: {v[0]} com {v[1]}')
    sleep (1)

    
    

    
    
