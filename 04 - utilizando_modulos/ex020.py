from random import shuffle

aluno01 = str(input('Aluno 01: '))
aluno02 = str(input('Aluno 02: '))
aluno03 = str(input('Aluno 03: '))
aluno04 = str(input('Aluno 04: '))
nomes = [aluno01,aluno02,aluno03,aluno04]
shuffle(nomes)
print('Ordem sorteada {}'.format(nomes))