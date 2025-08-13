dado = list()
pessoas = list()
resp = ''
pessoascadastradas = maior = menor = 0
while True:
    #Verificar o nome e o peso das pessoas e adicionar em uma lista, para cada pessoa terá uma lista diferente
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()
    #Verificar se o usuário quer continuar ou não e verificar se ele digitou as letras S/N para finalizar
    while True:
        resp = str(input('Quer continuar [S/N]: ')).upper().split()[0]
        if resp not in 'SN':
            resp = str(input('Quer continuar [S/N]: ')).upper().split()[0] 
        else:
            break   
    if resp in 'N':
        break
for p in pessoas:
    #Verificar quantas pessoas foram cadastradas
    pessoascadastradas  += 1
    #Verificar o maior peso
    if pessoascadastradas == 1:
        maior = p[1]
        menor = p[1]
    #Verificar o menor peso
    else:
        if p[1]>maior:
            maior = p[1]
        elif p[1] < menor:
            menor = p[1]
#Informa o maior peso e o nome das pessoas 
print(f'O maior peso foi de {maior:.2f}kg. Peso de ',end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}',end=' ')
print()
#Informa o menor peso e o nome das pessoas
print(f'O menor peso foi de {menor:.2f}kg. Peso de ',end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}',end=' ')
    




