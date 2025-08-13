from time import sleep
def contador():
    print('-='*20)
    print('Contagem de 1 até 10 de 1 em 1')
    for C in range(1,11):
        print(C,end=' ',flush=True)
        sleep(0.5)
    print('FIM!')
    print('-='*20)
    print('Contagem de 10 até 0 de 2 em 2')
    for C in range(10,-2,-2):
        print(C,end=' ',flush=True)
        sleep(0.5)
    print('FIM!')
    print('Agora é sua vez de personalizar a contagem!')
    I = int(input('Inicio: '))
    F = int(input('Fim: '))
    P = int(input('Passo: '))
    print('-='*20)
    if P == 0:
        P = 1
    elif P < 0:
        P = abs(P)
    print(f'Contagem de {I} até {F} de {P} em {P}')
    if I<F:
        for C in range(I,F+1,P):
            print(C,end=' ',flush=True)
            sleep(0.5)
        print('FIM!')
    elif I>F:
        for C in range(I,F-1,-P):
            print(C,end=' ',flush=True)
            sleep(0.5)
        print('FIM!')


#programaprincipal
contador()