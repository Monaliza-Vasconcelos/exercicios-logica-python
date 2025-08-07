cont = 0
expre = str(input('Digite uma expressão: '))
pilha = list()
for v in expre:
    if v == '(':
        pilha.append(v)
        cont += 1
    if v == ')':
        pilha.pop()
        cont -= 1
if cont == 0:
    print('Sua expressão é válida')
else:
    print('Sua expressão é inválida ')