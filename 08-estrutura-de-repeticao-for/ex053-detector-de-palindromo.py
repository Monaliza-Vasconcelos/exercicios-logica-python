frase = str(input('Digite uma frase e veja se ela é um palíndromo: ')).strip().replace(' ','').upper()
if (frase[::-1] == frase):
    print('É UMA FRASE PALÍNDROMO')
else:
    print('NÃO É UMA FRASE PALÍNDROMO')
