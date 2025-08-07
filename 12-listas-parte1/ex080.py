valores = list()
for C in range(0,5):
    if C == 0:
        valores.append(int(input('Digite um valor: ')))
        print('Adicionado ao final da lista... ')
    elif C == 1:
        N = int(input('Digite um valor: '))
        if N < valores[0]:
            valores.insert(0,N)
            print('Adicionado na posição 0')
        else:
            valores.append(N)
            print('Adicionado ao final da lista')
    elif C == 2:
        N = int(input('Digite um valor: '))
        if (N>valores[0] and (N<=valores[1])):
            valores.insert(1,N)
            print('Adicionado na posição 1')
        elif (N<valores[0]):
            valores.insert(0,N)
            print('Adicionado a posição 0')
        elif (N>valores[1]):
            valores.append(N)
            print('Adicionado ao final da lista ')
    elif C == 3:
        N = int(input('Digite um valor: '))
        if (N<valores[0]):
            print('Adicionado na posição 0')
            valores.insert(0,N)
        elif (N>valores[3]):
            valores.append(N)
            print('Adicionado ao final da lista0')
        elif (N>valores[0]) and (N<=valores[1]):
            valores.insert(1,N)
            print('Adicionado na posição 1')
        elif (N>valores[1]) and (N<=valores[2]):
            valores.insert(2,N)
            print('Adicionaddo na posição 2')
    elif C == 4:
        N = int(input('Digite um valor: '))
        if (N>valores[3]):
            valores.append(N)
            print('Adicionado ao final da lista')
        elif (N<valores[0]):
            valores.insert(0,N)
            print('Adicionado na posição 0')
        elif (N>valores[0]) and (N<=valores[1]):
            valores.insert(1,N)
            print('Adicionado na posição 1')
        elif (N>valores[1]) and (N<=valores[2]):
            valores.insert(2,N)
            print('Adicionado na posição 2')
        elif (N>valores[2]) and (N<=valores[3]):
            valores.insert(3,N)
            print('Adicionado na posição 3')
print(valores)

    