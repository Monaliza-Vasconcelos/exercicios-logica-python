
C = ('\033[m', # 0 Branco
    '\033[0;30;41m', # 1 Vermelho
    '\033[0;30;42m', # 2 Verde
    '\033[0;30;43m', # 3 Amarelo
    '\033[0;30;44m') # 4 Azul

def hel(com):
    ajustes(f'Acessando o manual do comando \'{com}\'',2)
    help(com)


def ajustes(linhas,cor=0):
    tam = len(linhas) + 4
    print(C[cor])
    print(f'~'*tam)
    print(f'  {linhas}')
    print(f'~'*tam)
    print(C[0])


#programa principal
comando = ''
while True:
    sistema = ajustes('Sistema de ajuda PYHelp',3)
    comando = input('Função ou Biblioteca > ')
    if comando.upper() == 'FIM':
        break
    else:
        hel(comando)
        
sistema = ajustes('ATÉ LOGO!',1)

