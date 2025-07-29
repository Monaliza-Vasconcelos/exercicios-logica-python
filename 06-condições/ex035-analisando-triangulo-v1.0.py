A = float(input('Valor de A: '))
B = float(input('Valor de B: '))
C = float(input('Valor de C: '))
if ((A+B)>C) and ((A+C)>B) and ((B+C)>A):
    print('Os valores {},{} e {}, podem formar um triângulo.'.format(A,B,C))
else:
    print('Os valores {},{} e {}, não podem formar um triângulo.'.format(A,B,C))