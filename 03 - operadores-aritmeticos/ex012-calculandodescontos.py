preco = float(input('Qual o valor do produto? '))
descont = float(preco*5/100)
total_a_pagar = preco-descont
print('O total a pagar com 5% de desconto é R${}'.format(total_a_pagar))