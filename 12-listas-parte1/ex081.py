valores = list()
quant = valor5 = 0
resp = ''
while True:
    valores.append(int(input('Digite um valor: ')))
    quant += 1
    resp = str(input('Deseja continuar? [S/N] ')).upper().split()[0]
    while True:
        if resp not in 'SN':
            print('Erro') 
            resp = str(input('Deseja continuar? [S/N] ')).upper().split()[0]
        else:
            break   
    if resp == 'N':
        break
for v in valores:
    if v == 5:
        valor5 += 1
valores.sort(reverse=True)
print(f'Foram digitados {quant} números')
print(f'Lista de forma decrescente {valores}')
if valor5 > 0:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')



