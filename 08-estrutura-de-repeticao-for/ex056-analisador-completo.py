soma = 0
media = 0
maioridade = 0
mulheres_com_menos_21 = 0
nomemaisvelho = ''

for C in range(1,5):
    nome = str(input('Qual seu nome? '))
    idade = float(input('Qual sua idade? '))
    sexo = str(input('Qual seu sexo [M/F]: ')).upper()
    soma += idade
    if (sexo == 'M'):
        if idade > maioridade:
            maioridade = idade
            nomemaisvelho = nome
    if (sexo == 'F'):
        if idade < 21:
            mulheres_com_menos_21 += 1
media = soma/4
print('A média de idade do grupo é {}'.format(media))
print('O homem mais velho do grupo é {}'.format(nomemaisvelho))
print('Quantidade de mulheres com menos de 21 anos: {}'.format(mulheres_com_menos_21))