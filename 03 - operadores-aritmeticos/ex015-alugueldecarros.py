dias_alugados = int(input('Quantos dias o carro foi alugado? '))
km_rodados = int(input('Quantos Km rodados? '))
total_por_dia = dias_alugados*60
total_por_km = 0.15*km_rodados
soma = float(total_por_dia+total_por_km)

print('O total a pagar é: {:.2f}'.format(soma))