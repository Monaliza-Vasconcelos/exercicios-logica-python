import os
os.system('cls')
print('\033[0;35;40mSEQUÊNCIA DE FIBONACCI\033[m')
N1 = 0
N2 = 1
aux = 0
C = 3
print('='*30)
N = int(input('Digite um número: '))
print('{} -> {}'.format(N1,N2),end=' -> ')
while C <= N:
    aux = N1 + N2
    print('{}'.format(aux),end=' -> ')
    N1 = N2
    N2 = aux
    C += 1
print('FIM')
print('=' *30)