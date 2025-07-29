salario_funcionario = float(input('Digite seu salário: '))
if salario_funcionario>1250:
    aumento = float(salario_funcionario*10/100)
    print('Seu novo salário com aumento de 10% será de R${:.2f}'.format(salario_funcionario+aumento))
else:
    aumento = float(salario_funcionario*15/100)
    print('Seu novo salário com aumento de 15% será de R${:.2f}'.format(salario_funcionario+aumento))