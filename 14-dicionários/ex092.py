
from datetime import datetime
pessoas = {}
ano_nas = ano_contra = 0
pessoas['nome'] = str(input('Nome: '))
ano_nas = int(input('Ano de nascimento: '))
pessoas['idade'] =  datetime.now().year - ano_nas
pessoas['ctps']  = int(input('Carteira de Trabalho (0 não tem): '))
if pessoas['ctps'] != 0: 
    pessoas['contratação'] = int(input('Ano de contratação: '))
    pessoas['Salário'] = float(input('Salário: R$'))
    pessoas['Aposentadoria'] = (pessoas['contratação'] + 35 - ano_nas)
for k,v in pessoas.items():
    print(f'{k} tem o valor {v}')