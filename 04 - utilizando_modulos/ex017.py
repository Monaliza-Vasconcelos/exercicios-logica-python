from math import hypot, sqrt
c_cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
c_cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
print('A hipotenusa de {} e {} é {:.1f}'.format(c_cateto_oposto,c_cateto_adjacente,hypot(c_cateto_oposto,c_cateto_adjacente)))
