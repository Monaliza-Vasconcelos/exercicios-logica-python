from random import randint
def maior(*N):
    cont = mai = 0
    print('Analisando os valores passados...')
    for C in N:
        print(f'{C}',end=' ')
        if cont == 0:
            mai = C
        else:
            if C > mai:
                mai = C
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {mai}.')


#Programa principal
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior(0)
