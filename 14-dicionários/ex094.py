import os
os.system('cls')
resp = ''
lista = []
soma = media = Totc =  mulheres_cada = 0
while True:
    dados = {}
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper().split()[0]
        if dados['sexo'] in 'MF':
            break
        else:
            print('ERRO')
    dados['idade'] = int(input('Idade: '))
    lista.append(dados)
    del dados
    while True:
        resp = str(input('Quer continuar [S/N]? ')).upper().split()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO')
    if resp == 'N':
        break
print('='*30)
for Q in range(0, len(lista)):
    Totc += 1
    soma += lista[Q]['idade']
media = soma/Totc
print(f'- O grupo tem {Totc} pessoas.')
print(f'- A média de idade é de {media:.2f}.')
print('- As mulheres cadastradas foram: ',end=' ')
for M in range(0,len(lista)):
    if lista[M]['sexo'] in 'F':
        print(lista[M]['nome'],end=' ')
print()
print('Lista das pessoas que estão acima da média: ')
print()
for M in range(0,len(lista)):
    if lista[M]['idade'] > media:
        print(f'nome = {lista[M]["nome"]}; sexo = {lista[M]["sexo"]}; idade = {lista[M]["idade"]};')
print('Encerrado')

        

