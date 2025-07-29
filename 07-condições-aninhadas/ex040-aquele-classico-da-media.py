N1 = float(input('Primeira Nota: '))
N2 = float(input('Segunda Nota: '))
media = (N1+N2)/2
if media <= 5:
    print('Sua média foi: {}'.format(media))
    print('REPROVADO!')
elif (media>5) and (media<=6.9):
    print('Sua média foi: {}'.format(media))
    print('RECUPERAÇÃO!')
elif (media>7) and (media<10):
    print('Sua média foi: {}'.format(media))
    print('APROVADO!')
else:
    print('Valor não aceitado!')