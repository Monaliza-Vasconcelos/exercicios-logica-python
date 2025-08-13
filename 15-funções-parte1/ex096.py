def area(larg,compri):
    a = 0
    a = larg * compri
    print(f'A área de um terreno {larg} x {compri} é de {a}m².')


#programa principal
print('Controle de Terrenos')
print('--------------------')
l = (float(input('LARGURA (m): ')))
c = (float(input('COMPRIMENTO (m): ')))
area(l,c)