import os
os.system('cls')
matriz = []
valores = []
cont = soma = somaterceira = maior = 0
#Receberá os valores da matriz e armazenará em três listas
for V in range(0,3):
    matriz.append(int(input(f'Digite um valor [{cont}, {V}]: ')))
valores.append(matriz[:])
matriz.clear()
cont = 1
for V in range(0,3):
    matriz.append(int(input(f'Digite um valor [{cont}, {V}]: ')))
    if V == 0:
        maior = matriz[V]
    elif matriz[V] > maior:
        maior = matriz[V]
valores.append(matriz[:])
matriz.clear()
cont = 2
for V in range(0,3):
    matriz.append(int(input(f'Digite um valor [{cont}, {V}]: ')))
valores.append(matriz[:])
matriz.clear()
#Realizará a varredura para organização dos valores em forma de matriz
print('=-'*30)
for E in valores:
    #Pega o último valor de cada lista que no caso fica sendo a terceira coluna
    somaterceira += E[-1]
    for V in E:  
        print(f'[ {V} ]',end=' ')
        #Ralizará a adição dos números pares de todas as três listas
        if V % 2 == 0:
            soma += V
    print()
print('=-'*30)
print(f'A soma dos valores pares é {soma}. ')
print(f'A soma dos valores da terceira coluna é {somaterceira}. ')
print(f'O maior valor da segundo linha é {maior}. ')
    


