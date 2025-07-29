print('Descobrindo números primos')
resul = 0
N = int(input('Digite um número: '))
for C in range(N,0,-1):
    if (N%C==0):
        resul += 1
if resul == 2:
    print('{} é um número primo'.format(N))
else:
    print('{} não é um número primo'.format(N))