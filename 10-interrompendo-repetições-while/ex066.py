soma = totn = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    soma += n
    totn += 1
print(f'O resultado da soma dos valores digitados foi {soma}')
print(f'O total de números digitados foi: {totn}')