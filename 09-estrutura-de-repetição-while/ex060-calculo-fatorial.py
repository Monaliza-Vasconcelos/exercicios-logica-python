N = int(input('Digite um número para calcular o fatorial: '))
C = N
F = 1
print('Calculando {}! = '.format(C),end=' ')
while C > 0:
    if C > 1:
        print(C, 'x',end=' ')
    else:
        print(C, '=',end=' ')
    F *= C
    C -= 1
print(F)
