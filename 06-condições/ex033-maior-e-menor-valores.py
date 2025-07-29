N1 = int(input('Primeiro número: '))
N2 = int(input('Segundo número: '))
N3 = int(input('Terceiro número: '))

if (N1>N2) and (N1>N3):
    print('Maior número: {}'.format(N1))
elif (N2>N1) and (N2>N3):
    print('Maior número: {}'.format(N2))
else:
    print('Maior número: {}'.format(N3))

if (N1<N2) and (N1<N3):
    print('Menor número: {}'.format(N1))
elif (N2<N1) and (N2<N3):
    print('Menor número: {}'.format(N2))
else:
    print('Menor número: {}'.format(N3))
