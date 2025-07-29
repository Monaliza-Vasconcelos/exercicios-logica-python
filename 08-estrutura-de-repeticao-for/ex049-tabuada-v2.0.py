import os
os.system('cls')
N = int(input('Digite um número entre 1 e 10 e veja a tabuada: '))
for C in range(1,11):
    print('{} x {} = {}'.format(N,C,N*C))