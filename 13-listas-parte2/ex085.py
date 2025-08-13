V =  0
N = [[],[]]
# Perguntar os números que a pessoa quer digitar e verificar se ele é par ou ímpar
# Os valores serão armazenados em duas listas dentro de uma maior como par e ímpar
for C in range(1,8):
    V = (int(input(f'Digite o {C}º valor: ')))
    if V % 2 == 0:
        N[0].append(V)    
    else:
        N[1].append(V)
#Saida dos valores digitados organizados nas suas respectivas listas
print (f'Os valores pares digitados foram: {sorted(N[0])}')
print(f'Os valores ímpares digitados foram: {sorted(N[1])}')



