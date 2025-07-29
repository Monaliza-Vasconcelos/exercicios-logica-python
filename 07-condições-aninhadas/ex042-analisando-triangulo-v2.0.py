A = float(input('Digite o valor de A: '))
B = float(input('Digite o valor de B: '))
C = float(input('Digite o valor de C: '))
if (A+B>C) and (A+C>B) and (C+B>A):
    print('Pode formar um triângulo.')
    if (A!=B) and (A!=C) and (B!=C):
        print('E é ESCALENO')
    elif (A==B) and (A==C):
        print('E é EQUILÁTERO')
    else:
        print('E é ISÓSCELES')
else:
    print('Não pode formar um triângulo.')