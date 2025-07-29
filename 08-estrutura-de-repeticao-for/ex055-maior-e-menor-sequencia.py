maior = 0
menor = 0
for C in range(1,6):
    peso = float(input('Qual seu peso: '))
    if C == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso digitado foi: {}'.format(maior))
print('O menor peso digitado foi {}'.format(menor))