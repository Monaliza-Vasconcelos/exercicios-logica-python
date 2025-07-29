distancia_km = float(input('Qual a distância da viagem em km? '))
if distancia_km<=200:
    valor = distancia_km*0.50
else:
    valor = distancia_km*0.45
print('O valor a pagar é R${:.2f} reais'.format(valor))
