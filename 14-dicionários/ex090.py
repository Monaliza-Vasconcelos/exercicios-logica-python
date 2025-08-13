sit = {}
sit['Nome'] = str(input('Qual seu nome? '))
sit['Média'] = float(input(f'Qual sua média, {sit["Nome"]}: '))
if sit['Média'] >= 7:
    sit['situacao'] = 'Aprovado'
elif sit['Média'] < 7 and sit['Média'] > 5:
    sit['situacao'] = 'Recuperação'
else:
    sit['situacao'] = 'Reprovado'
for k,v in sit.items():
    print(f'{k} é a {v}')