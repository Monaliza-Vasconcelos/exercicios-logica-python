from random import randint

N = randint(0,10)
C = True
Contagem = 0
while C == True:
    Num = int(input('Digite um número e tente acertar: '))
    Contagem += 1
    if Num == N:
        C = False
print('Parabéns, você acertou, mas precisou de {} tentativas'.format(Contagem))