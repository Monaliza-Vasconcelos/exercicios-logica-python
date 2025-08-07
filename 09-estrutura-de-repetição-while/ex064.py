import os
os.system('cls')
C = ToTN = Soma = 0
while C != 999:
    C = int(input('Digite um número [999 para parar]: '))
    if C != 999:
        ToTN += 1
        Soma += C
print('Total de números digitados: {}'.format(ToTN))
print('A soma dos números digitados é: {}'.format(Soma))
