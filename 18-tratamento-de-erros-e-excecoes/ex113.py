def leiaint(R):
    """
        -> Verificando se o número é inteiro
        :param R: Recebe a frase de n e dentro da função pergunta ao 
        usuário o número, retornando ao programa principal

    """
    while True:
        try:
            X = (input(R))
            if X == '':
                print('\033[0;31mUsuário preferiu não digitar esse número.\033[m')
                return 0
            else:
                X = int(X)
                return X
        except (ValueError,TypeError):
            print('\033[0;31mOPS, você digitou um valor errado, tente novamente\033[m')

def leiaFloat(F):
    """
        :param F: Recebe um valor 
        :return: Retorna um valor de ponto flutuante
    """
    while True:
        try:
            X =(input(F))
            if X == '':
               print('\033[0;31mUsuário preferiu não digitar esse número.\033[m')
               return 0
            else:
                X = float(X)
                return X
        except (ValueError,TypeError):
            print('\033[0;31mOPS, você digitou um valor errado, tente novamente.\033[m')
        
#programaprincipal
n = leiaint('Digite um número inteiro: ')
nf = leiaFloat('Digite um número com ponto flutuante: ')
print(f'O valor inteiro digitado foi {n} e o real foi {nf}')