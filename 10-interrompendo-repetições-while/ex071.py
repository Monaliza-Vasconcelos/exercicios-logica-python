tot50 = soma50 = soma20 = soma10 = soma1 = valor = tot20 = tot10 = 0
print('='*40)
print('BANCO CEV'.center(40))
print('='*40)
valor = float(input('Que valor você quer sacar? R$ '))
while valor != 0:
    tot50 = 50
    if valor >= tot50:
        valor -= tot50
        soma50 += 1
    elif valor >=20:
        tot20 = 20
        valor -= tot20
        soma20 += 1
    elif valor >= 10:
        tot10 = 10
        valor -= tot10
        soma10 += 1
    elif valor >= 1:
        tot1 = 1
        valor -= tot1
        soma1 += 1
print(f'Total de {soma50} cédulas de R$50 sacadas')
print(f'Total de {soma20} cédulas de R$20 sacadas')
print(f'Total de {soma10} cédulas de R$10 sacadas')
print(f'Total de {soma1} cédulas de R$1 sacadas')
