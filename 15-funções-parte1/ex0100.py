from random import randint
def sorteio(lista):
    print(f'Sorteando 5 valores da lista : ',end=' ')
    for C in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n}',end=' ')
    print('PRONTO!')
def somapar(lista):
    soma = 0
    for C in lista:
        if C%2==0:
            soma += C
    print(f'Somando os valores pares de {numeros}',end=' ')
    print(f', temos {soma}')



#programaprincipal
numeros = list()
sorteio(numeros)
somapar(numeros)