tabela = {}
gols = []
partidas = soma = cont = 0
#Inicialização para preencher a tabela
tabela['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {tabela["Nome"]} jogou? '))
#Realizar uma contagem até a quantidade de partidas que o jogador jogou com for 
for P in range(0,partidas):
    gols.append(int(input(f'Quantos gols na partida {P}? ')))
tabela['gols'] = gols[:]
#Somar os gols realizados pelo jogador
for G in gols:
    soma += G
tabela['total'] = soma
print('-='*40)
#Realizar a varredura e mostrar os campos de chaves e valores
for K,V in tabela.items():
    print(f'O campo {K} tem o valor {V}. ')
print('-='*40)
print(f'O jogador {tabela["Nome"]} jogou {partidas} partidas. ')
for cont, G in enumerate(gols):
    print(f'=> Na partida {cont}, fez {G} gols.')
print(f'Foi um total de {soma} gols. ')

