nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiuscula é: ',nome.upper())
print('Seu nome em minusculas é: ',nome.lower())
print('Seu nome tem {} letras'.format(len(nome.replace(' ',''))))
#print ('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0],len(separa[0])))
#print('Seu nome primeiro nome é {} e tem letras'.format(separa[0],))