from random import randint
contagem = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print('Os valores sorteados foram: ',end=' ')
for C in range (0,5):
    print(contagem[C],end=' ')
print()
sequencia = sorted(contagem)
print(f'O menor valor sorteado foi {sequencia[0]}')
print(f'O maior valor sorteado foi {sequencia[4]}')

