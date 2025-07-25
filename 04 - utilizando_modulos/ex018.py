import math 
N = float(input('Digite um valor: '))
cosseno = math.cos(math.radians(N))
seno = math.sin(math.radians(N))
tangente = math.tan(math.radians(N))
print('Valor convertido para cosseno: {:.2f}'.format(cosseno))
print('Valor convertido para seno: {:.2f}'.format(seno))
print('Valor convertido para tangente: {:.2f}'.format(tangente))