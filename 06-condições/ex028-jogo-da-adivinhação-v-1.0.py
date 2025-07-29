import random
n_sorteado = (random.randint(0,5))
N = int(input(('Digite um valor entre 0 e 5: ')))
print('PROCESSANDO...')
if N == n_sorteado:
    print('Parabéns, você acertou!')
else:
    print('O computador venceu!')