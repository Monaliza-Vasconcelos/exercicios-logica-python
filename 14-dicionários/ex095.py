import os
os.system('cls')
partidas = 0
resp = ''
dados = []
#Inicio da estrutura de repeção while
while True:
    tabela = {}
    gols = []
    soma = 0
    print('-'*40)
    #Incluir os nomes dos jogadores dentro do dicionário com a chave Nome
    tabela['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {tabela["Nome"]} jogou? '))
    #Os gols irão ficar especialmente dentro de uma lista, dentro do dicionário com a chave gols
    for P in range(0,partidas):
        gols.append(int(input(f'Quantos gols na partida {P}? ')))
    tabela['gols'] = gols.copy()
    #Soma para obter o total de gols
    for T in gols:
        soma += T
    tabela['total'] = soma
    dados.append(tabela.copy())
    while True:
        resp = (str(input('Quer continuar [S/N]? '))).upper().split()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO')
    if resp in 'N':
        break
print('-='*20)
print(f'cod '.ljust(5),'nome'.ljust(15),'gols'.ljust(20),'total')
print('-'*50)
#Realizar a enumeração da lista de jogadores, com nomes, gols feitos e total
for I,V in enumerate(dados):
    gols_str = str(dados[I]["gols"])
    print(f'{I:<5} {dados[I]["Nome"]:<15} {gols_str:<20} {dados[I]["total"]}')
compdados = len(dados)
#Essa estrutura de repetição é para mostrar o aproveitamento do jogador que o usuário deseja ver
while True:
    R = int(input('Mostrar dados de qual jogador? '))
    if R == 999:
        break
    while R >= len(dados):
        print(f'Erro, não existe jogador com código {R}')
        R = int(input('Mostrar dados de qual jogador? '))
        if R == 999:
            break
    if R == 999:
        break
    print(f'--Levantamento do jogador {dados[R]["Nome"]}: ')
    for C,J in enumerate(dados[R]['gols']):
        print(f'No jogo {C} fez {dados[R]["gols"][C]} gols.')
    
    
    
        


