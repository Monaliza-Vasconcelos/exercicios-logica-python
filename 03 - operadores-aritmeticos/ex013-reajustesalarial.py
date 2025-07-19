salario = float(input('Qual seu salário? '))
reajuste = float(salario*15/100)
valor_com_aumento = float(salario+reajuste)
print('Seu novo salário com aumento de 15% é de: R${}'.format(valor_com_aumento))