import os
os.system('cls')
totgasto =  maisde1000 = C = menorvalor = 0
menorvalornome = ''
print('-'*40)
print('LOJA SUPER BARATÃO'.center(40))
print('-'*40)
while True:
    C +=1
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: '))
    totgasto += preco
    if preco > 1000.00:
        maisde1000 += 1
    if C == 1:
        menorvalor = preco
    if preco < menorvalor:
        menorvalor = preco
        menorvalornome = produto
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'\033[0;34;40m-\033[m'*40)
print(f'Total de gasto na compra R${totgasto:.2f}')
print(f'Produtos que custam mais de R$1.000 reais: {maisde1000}')
print(f'Produto mais barato foi {menorvalornome}, que custa R${menorvalor} reais')

