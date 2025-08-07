from random import randint
import os
os.system('cls')
soma = tot = 0
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
while True:
    computador = randint(1,10)
    n = int(input('Diga um valor: '))
    soma = computador + n
    ParOuImpar = str(input('Par ou ímpar? [P/I]: ')).upper().strip()[0]
    while ParOuImpar not in 'PI':
        ParOuImpar = str(input('Par ou ímpar? [P/I]: ')).upper().strip()[0]
    if (soma % 2 == 0):
        if ParOuImpar == 'P':
            tot += 1
            print('-'*30)
            print(f'Você jogou {n} e o computador {computador}. Total de {soma} e DEU PAR')
            print('-'*30)
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('=-'*15)
        elif ParOuImpar == 'I':
            print('-'*30)
            print(f'Você jogou {n} e o computador {computador}. Total de {soma} e DEU PAR')
            print('-'*30)
            print('Você PERDEU')
            print('=-'*15)
            break
    if (soma % 2 == 1):
        if ParOuImpar == 'I':
            tot += 1
            print('-'*30)
            print(f'Você jogou {n} e o computador {computador}. Total de {soma} e DEU ÍMPAR')
            print('-'*30)
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
        elif ParOuImpar == 'P':
            print('-'*30)
            print(f'Você jogou {n} e o computador {computador}. Total de {soma} e DEU ÍMPAR')
            print('-'*30)
            print('Você PERDEU')
            print('=-'*15)
            break

print(f'GAME OVER! Você venceu {tot} vezes.')