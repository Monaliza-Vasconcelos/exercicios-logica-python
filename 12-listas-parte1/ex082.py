valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar [S/N] ')).upper().split()[0]
    while True:
        if resp not in 'SN':
            print('erro')
            resp = str(input('Deseja continuar [S/N] ')).upper().split()[0]
        else:
            break
    if resp == 'N':
        break

#Verificar se os valores da lista são pares ou ímpares e jogar em duas outras listas
valorespar = list()
valoresimpar = list ()
for v in valores:
    if v%2 == 0:
        valorespar.append(v)
    elif v%2==1:
        valoresimpar.append(v)
#Saída dos elementos que têm nas listas
print(f'A lista completa é {valores}')
print(f'Valores pares digitados {valorespar}')
print(f'Valores ímpares digitados {valoresimpar}')