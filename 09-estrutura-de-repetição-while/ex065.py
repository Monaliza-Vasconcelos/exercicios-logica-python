import os
os.system('cls')
C = 'S'
Cont = Soma = Maior = 0
Menor = 9999999999999999999
while C in 'S':
    N = int(input('Digite um número: '))
    C = str(input('Quer continuar? [S/N]: ')).upper()
    Soma += N
    Cont += 1
    if Cont == 1:
        Maior = Menor = N
    else:
        if N> Maior:
            Maior = N
        if N < Menor:
            Menor = N
Media = Soma/Cont
print('A média dos valores digitados é: {}'.format(Media))
print('O maior número digitado foi: {}'.format(Maior))
print('O menor número digitado foi {}'.format(Menor))
    
