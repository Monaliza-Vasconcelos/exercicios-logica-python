print('\033[0;32;40m-Formas de pagamento-\033[;;m')
print('\033[0;32;40m[1]\033[;;m A VISTA/DINHEIRO/CHEQUE')
print('\033[0;32;40m[2]\033[;;m CARTÃO A VISTA')
print('\033[0;32;40m[3]\033[;;m ATÉ 2X NO CARTÃO')
print('\033[0;32;40m[4]\033[;;m 3X OU MAIS')
forma_de_pagamento = str(input('Qual será sua forma de pagamento? ')).upper().strip()
valor_da_compra = float(input('Qual o valor da compra? '))
if forma_de_pagamento == '1':
    desconto = valor_da_compra*10/100
    tot = valor_da_compra - desconto
    print('O valor da sua compra foi R${:.2f} reais e como foi pago a vista, você recebe 10% de desconto, o valor a pagar é: R${:.2f} reais'.format(valor_da_compra,tot))
elif forma_de_pagamento == '2':
    desconto = valor_da_compra*5/100
    tot = valor_da_compra - desconto
    print('O valor da sua compra foi R${:.2f} reais e como foi pago a vista no cartão, você recebe 5% de desconto, o valor a pagar é: R${:.2f} reais'.format(valor_da_compra,tot))
elif forma_de_pagamento == '3':
    print('Você não recebeu nenhum desconto, o valor a pagar é: {:.2f} reais'.format(valor_da_compra))
elif forma_de_pagamento == '4':
    juros = valor_da_compra*20/100
    tot = valor_da_compra + juros
    print('O valor da sua compra foi R${:.2f} reais e como foi pago de 3X, tem um juros de 20%, valor a pagar é: R${:.2f} reais'.format(valor_da_compra,tot))