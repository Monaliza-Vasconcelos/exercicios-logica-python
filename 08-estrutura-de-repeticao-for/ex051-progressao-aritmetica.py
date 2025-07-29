import os
os.system('cls')
an = 1
n = 1
print('=======================')
print('  10 TERMOS DE UMA PA  ')
print('=======================')
a = int(input('1º Termo: '))
r = int(input('Razão: '))
for C in range(1,11):
    an = a + (C-1)*r
    print(an,end=' -> ')
print('ACABOU')