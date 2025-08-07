V = list()
resp = ''
while True:
    valor = int(input('Digite um valor: '))
    if V.count(valor) == 0:
        V.append(valor)
        print('Valor adicionado com sucesso! ')
        resp = str((input('Quer continuar? [S/N] '))).upper().split()[0]
        while True:
            if resp not in 'SN':
                resp = str((input('Quer continuar? [S/N] '))).upper().split()[0]
            else:
                break     
        if resp == 'N':
            break 
    else:
        print('Valor duplicado, não vou adicionar! ')
        resp = str((input('Quer continuar? [S/N] '))).upper().split()[0]
        while True:
            if resp not in 'SN':
                resp = str((input('Quer continuar? [S/N] '))).upper().split()[0]
            else:
                break     
        if resp == 'N':
            break 
print(f'Os valores digitados foram: {sorted(V[0:])}')