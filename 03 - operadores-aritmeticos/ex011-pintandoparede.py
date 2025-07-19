largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
calculo_de_tintas = int(altura*largura)
total_de_latas = int(calculo_de_tintas/2)

print('Será necessário {} latas de tinta para pintar a parede, com {} metros quadrados'.format(total_de_latas,calculo_de_tintas))