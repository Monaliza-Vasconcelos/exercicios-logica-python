def leiaint(R):
    """
        -> Verificando se o número é inteiro
        :param R: Recebe a frase de n e dentro da função pergunta ao 
        usuário o número, retornando ao programa principal

    """
    while True:
        X = input(f'{R}')
        if X.isdigit():
            return X
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
    
        
#programaprincipal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
