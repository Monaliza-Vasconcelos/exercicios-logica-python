sexo = str(input('Qual seu sexo? [M/F]: ')).upper().strip()
while sexo not in 'MF':
    sexo = str(input('Digitação errada, escolha [M/F]: ')).upper().strip()
print('Sexo {} registrado com sucesso!'.format(sexo))
