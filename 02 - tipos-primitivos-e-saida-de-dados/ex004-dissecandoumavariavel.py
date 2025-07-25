nome = input('Qual seu nome')
print(type(nome))
print('É numerico? ',nome.isnumeric()) #Se é númerico ou não
print('É letra? ',nome.isalpha()) #Se é letra ou não
print('É alfabetico? ',nome.isalnum()) #Se é alfabetico ou númerico
print('Tem somente letras maiusculas? ',nome.isupper()) #Se está somente com letras maiusculas
print('Tem somente letras minusculas? ',nome.islower()) #Se está todas em minusculas
print('Contém somente espaços? ',nome.isspace()) #Se contém somente espaços