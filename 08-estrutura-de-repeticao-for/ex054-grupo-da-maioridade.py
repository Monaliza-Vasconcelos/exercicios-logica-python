from datetime import date
ano_atual = 0
maioridade = 0
menoridade = 0

for C in range(1,8):
    ano_nas = int(input('Digite o ano do seu nascimento: '))
    ano_atual = date.today().year
    idade = ano_atual - ano_nas
    if (idade>=21):
        maioridade += 1
    else:
        menoridade += 1
print('Quantidade de pessoas que são maiores de idade: {}'.format(maioridade))
print('Quantidade de pessoas que são menores de idade: {}'.format(menoridade))
