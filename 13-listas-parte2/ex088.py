import os
from time import sleep
from random import randint
os.system('cls')
J = 0
N = 0
print('-'*40)
print('JOGO NA MEGA SENA'.center(40))
print('-'*40)
jogos = []
N = (int(input('Quantos jogos você quer que eu sorteie? ')))
print('-='*5,f'SORTEANDO {N} JOGOS','-='*5)
for V in range(N):
    jogos.append([randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60)])
    print(f'Jogo {V+1} {jogos[V]}')
print('BOA SORTE'.center(40))
    
    

