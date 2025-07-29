from datetime import date
ano_nasc = int(input('Digite o ano do seu nascimento: '))
ano_hoje = date.today().year
idade = ano_hoje - ano_nasc
if idade <= 9:
    print('MIRIM')
elif (idade>9) and (idade<=14):
    print('INFANTIL')
elif (idade>14) and (idade<=19):
    print('JUNIOR')
elif (idade>19) and (idade<=20):
    print('SÊNIOR')
else:
    print('MASTER')

