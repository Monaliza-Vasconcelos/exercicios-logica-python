from datetime import date
ano_nasc = int(input('Qual o ano em que você nasceu? '))
ano = date.today().year
calculo = ano-ano_nasc
anos_que_falta = 18 - calculo
anos_que_passou = calculo -18
if calculo < 18:
    print('Ainda vai se alistar ao serviço militar.')
    print('Ainda faltam {} anos par o alistamento.'.format(anos_que_falta))
elif calculo == 18:
    print('É a hora de se alistar.')
else:
    print('Passou da hora de se alistar.')
    print('Passaram-se {} anos que você fez o alistamento.'.format(anos_que_passou))