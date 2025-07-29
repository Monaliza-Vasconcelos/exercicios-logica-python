
from datetime import date
ano = int(input('Quer analisar? Digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if (ano%4==0) and (ano%400==0):
    print('O ano {} é um ano BISSEXTO'.format(ano))
else:
    print('O ano de {} Não é um ano BISSEXTO'.format(ano))