import os
os.system('cls')
lista = [[]]
resp = nome = ''
n1 = n2 = media = resp2 = 0
while True:
    nome = (str(input('Nome: ')))
    n1 = (float(input('Nota 1: ')))
    n2 = (float(input('Nota 2: ')))
    media = (n1 + n2)/2
    lista[0].append([[nome],n1,n2,media])
    resp = (str(input('Deseja continuar: [S/N]: '))).upper().split()[0]
    if resp not in 'SN':
        while True:
            resp = (str(input('Deseja continuar: [S/N]: '))).upper().split()[0]  
            if resp in 'SN':
                break 
    elif resp == 'N':
        break
print(f'=-'*40)
print(f'Nº.'.ljust(6), 'NOME'.ljust(15),'MÉDIA'.ljust(10))
print(f'-'*40)
for V in range(len(lista[0])):
    print(f'{V:<6} {lista[0][V][0][0]:<15} {lista[0][V][3]:<10.1f}')
print(f'-'*40)
while True:
    resp2 = int(input('Quer mostrar as notas de qual aluno? (999 interrompe): '))
    if resp2 == 999:
        break
    else:
        print(f'Notas de {lista[0][resp2][0][0]} são [{lista[0][resp2][1]}, {lista[0][resp2][2]}]')
print('FINALIZANDO...')
print('<'*(5),'VOLTE SEMPRE','>'*(5))
