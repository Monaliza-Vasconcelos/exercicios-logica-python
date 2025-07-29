print('Emprestimo do Banco do Brasil')
valor_casa = float(input('Qual o valor da casa? '))
salario_do_comprador = float(input('Qual o salário do comprador? '))
anos_a_pagar = int(input('Em quantos anos você irá pagar? '))
valor_da_prestacao = valor_casa/(anos_a_pagar*12)
porcentagem_30_do_salario = salario_do_comprador*30/100
if valor_da_prestacao <= porcentagem_30_do_salario:
    print('Empréstimo aprovado! ')
else:
    print('Empréstimo negado! ')
