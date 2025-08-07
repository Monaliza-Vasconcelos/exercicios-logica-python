print('='*40)
print('TABELA DO BRASILEIRÃO'.center(40))
print('='*40)
tabela = ('Flamengo','Cruzeiro','Bragantino','Palmeiras','Bahia','Fluminence','Atletico-MG','BotaFogo','Mirassol','Corinthians','Grêmio','Ceará CS','Vasco da Gama','São Paulo','Santos','EC vitória','Internacional','Fortaleza','Juventude','Sport Recife')
#Mostrar os 5 primeiros colocados
print('\033[0;34;40mOs cinco primeiros colocados: \033[m')
for C in range (0,5):
    print(tabela[C])
print('\033[0;34;40mOs últimos quatro colocados: \033[m')
for C in range (4,0,-1):
    print(tabela[-C])
print('\033[0;34;40mTodos os times em ordem alfabética: \033[m')
sorteado = sorted(tabela)
for C in range(0,20):
    print(sorteado[C],end=' ')
print()
print('='*40)
for C in range(0,20):
    if (tabela[C] == 'Mirassol'):
        print(f'O time {tabela[C]} está na {C}ª posição')
