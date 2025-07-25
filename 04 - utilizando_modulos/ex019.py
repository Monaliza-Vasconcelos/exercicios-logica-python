from random import choice

aluno01 = str(input('Aluno 01: '))
aluno02 = str(input('Aluno 02: '))
aluno03 = str(input('Aluno 03: '))
aluno04 = str(input('Aluno 04: '))
sorteio = [aluno01,aluno02,aluno03,aluno04]
sorteio2 = choice(sorteio)
print('O aluno(a) sorteado(a) foi {}'.format(sorteio2))