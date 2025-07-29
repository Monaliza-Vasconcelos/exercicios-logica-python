soma = 0
Q = 0
for C in range(1,501):
    if (C%3==0) and (C%2==1):
        soma += C
        Q += 1
print('A soma entre {} números ímpares e que são múltiplos de três é: {}'.format(Q,soma))