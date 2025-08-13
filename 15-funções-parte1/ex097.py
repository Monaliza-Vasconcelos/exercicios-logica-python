def escreva(t):
    texto = []
    cont = 0
    texto.append(t)
    for c in texto:
        for i in c:
            cont += 1
    print('~'*cont)
    print(t)
    print('~'*cont)
    

#programaprincipal
escreva('Curso de python no Youtube')
escreva('Monaliza Vasconcelos')
escreva('CeV')