maior = menor = 0
valores = list()
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor {cont}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]   
print(f'O maior valor digitado foi {maior} nas posicoes ',end=' ')
for cont in range(0,5):
    if valores[cont] == maior:
        print(f'{cont}',end=' ')
print()
print(f'O menor valor digitado foi {menor} nas posições ',end=' ')
for cont in range (0,5):
    if valores[cont] == menor:
        print(f'{cont}',end=' ')



