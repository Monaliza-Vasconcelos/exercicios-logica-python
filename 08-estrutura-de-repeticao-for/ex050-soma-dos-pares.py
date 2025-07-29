
soma = 0
for C in range(1,7):
    N = int(input('Digite um número inteiro: '))
    if N%2==0:
        soma += N
print('A soma dos números pares digitados foi {}'.format(soma))