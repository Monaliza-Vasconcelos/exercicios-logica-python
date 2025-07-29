import math
N = int(input('Digite um número inteiro: '))
Resp = str(input('Deseja converter o número para binário, octal ou hexadecimal? ')).upper().strip()
N_binario = bin(N)[2:]
N_hexa = hex(N)[2:]
N_octa = oct(N)[2:]
if Resp == 'BINARIO':
    print('O número {} em binário é: {}'.format(N,N_binario))
elif Resp == 'HEXADECIMAL':
    print('O número {} em hexadecimal é: {}'.format(N,N_hexa))
else:
    print('O número {} em octal é: {}'.format(N,N_octa))
