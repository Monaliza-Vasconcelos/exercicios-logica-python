velocidade_docarro = float(input('Qual a velocidade que o carro vinha? '))
if velocidade_docarro>80:
    print('Você foi multado, ultrapassou a velocidade permitida.')
    multa = float((velocidade_docarro-80)*7)
    print('A multa a pagar é de R${:.2f} reais'.format(multa))
