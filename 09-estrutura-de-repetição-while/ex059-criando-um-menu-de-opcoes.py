import os
from time import sleep
os.system('cls')
C = True
Maior = 0
N1 = float(input('Digite um valor: '))
N2 = float(input('Digite outro valor: '))
while C == True:
    sleep(4)
    os.system('cls')
    print('ESCOLHA UMA OPÇÃO: ')
    print('\033[0;35;40m[1]\033[m Somar')
    print('\033[0;35;40m[2]\033[m Multiplicar')
    print('\033[0;35;40m[3]\033[m Maior')
    print('\033[0;35;40m[4]\033[m Novos números')
    print('\033[0;35;40m[5]\033[m Sair do programa')
    print('Valores digitados [{}] e [{}]'.format(N1,N2))
    res = int(input('Digite uma opção: '))
    if res not in(1,2,3,4,5):
        print('Resposta inválida, escolha uma outra opção')
    else:
        if res == 1:
            print('A soma entre {} e {} é {}'.format(N1,N2,N1 + N2))
        elif res == 2:
            print('Multiplicando os valores {} e {} obteremos o resultado {}'.format(N1,N2,N1*N2))
        elif res == 3:
            if(N1>N2):
                Maior = N1
                print('O maior número entre {} e {} é {}'.format(N1,N2,Maior))
            elif (N2>N1):
                Maior = N2
                print('O maior número entre {} e {} é {}'.format(N1,N2,Maior))
            else:
                print('Não existe valor maior entre {} e {}, os dois são iguais'.format(N1,N2))
        elif res == 4:
            os.system('cls')
            N1 = float(input('Digite um valor: '))
            N2 = float(input('Digite outro valor: '))
        elif res == 5:
            print('SAINDO',end='.')
            sleep(1.5)
            print(end='.')
            sleep(1.5)
            print(end='.')
            sleep(1.5)
            print(end='.')
            C = False