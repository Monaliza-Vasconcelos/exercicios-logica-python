import os
os.system('cls')
print('\033[0;35;40mDESCOBRINDO VALORES DOS TERMOS DE UMA PA\033[m')
a1 = int(input('Digite o 1º termo da PA: '))
r = int(input('Digite a razão da PA: '))
n = 1
res = True
T = 0
mais = 10
while res == True:
    while n <=10:
        an = a1 + (n-1)*r
        if n == 10:
            print(an, end='')
        else:
            print(an, end=' → ')
        n+=1
    print()
    tot = str((input('Deja continuar? [S/N]: '))).upper()
    if tot == 'N':
        res = False
    else:
        T = int(input('Deseja motrar quantos termos a mais? '))
        tot2 = mais + T
        while mais <= tot2-1:
            an = a1 + (mais-1)*r
            if mais == tot2-1:
                print(an, end='')
            else:
                print(an,end=' → ')
            mais += 1
print('\033[0;35;40m→ FIM\033[m')
