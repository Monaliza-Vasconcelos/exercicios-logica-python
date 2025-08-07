print('-'*40)
print('LISTAGEM DE PREÇOS'.center(40))
print('-'*40)
produtos = ('Lápis',1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25.00,'Transferidor',4.20,'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livro',34.90)
for C in range (0,len(produtos)):
    if C % 2 == 0:
        print(f'{produtos[C]:.<30}',end=' ')
    elif C % 2 == 1:
        print(f'RS{produtos[C]:>7.2f} ')
print('-'*40)
