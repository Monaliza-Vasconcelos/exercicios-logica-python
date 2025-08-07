contagem = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
N = int(input('Digite um número entre 0 e 20: '))
while True:
    if (N < 0) or (N>20):
        N = int(input('Digite um número entre 0 e 20: '))
    else:
        break
print(f'Você digitou o número {contagem[N]}')

