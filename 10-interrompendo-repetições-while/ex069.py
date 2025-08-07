import os
os.system('cls')
maior18 = homenscadastrados =  menor20 = 0
while True:
    print('\033[0;34;40m-\033[m'*30)
    print('CADASTRE UMA PESSOA')
    print('\033[0;34;40m-\033[m'*30)
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Qual seu sexo? M/F: ')).upper().strip()[0]
    while sexo  not in 'MF':
        sexo = str(input('Qual seu sexo? M/F: ')).upper().strip()[0]
    print('\033[0;34;40m-\033[m'*30)
    if idade>18:
        maior18 +=1
    if sexo == 'M':
        homenscadastrados += 1
    if (sexo == 'F') and (idade < 20):
        menor20 += 1
    resp = str(input('Quer continuar? S/N: ')).upper().strip()[0]
    while resp  not in 'SN':
         resp = str(input('Quer continuar? S/N: ')).upper().strip()[0]
    if resp == 'N':
        break
print('\033[0;34;40m-\033[m'*30)
print(f'Pessoas com mais de 18 anos: {maior18}')
print(f'Quantidade de homens cadastrados: {homenscadastrados}')
print(f'Mulheres com menos de 20 anos: {menor20}')
print('\033[0;34;40m-\033[m'*30)