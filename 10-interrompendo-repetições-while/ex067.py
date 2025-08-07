import os
os.system('cls')
n = 0
cont = 1
while True:
        n = int(input('Quer ver a tabuada de qual valor?'))
        print('-'*40)
        if n < 0:
            break
        for cont in range(1,11):
            print(n ,' x ',cont,f' = {n*cont}')
        print('-'*40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')


