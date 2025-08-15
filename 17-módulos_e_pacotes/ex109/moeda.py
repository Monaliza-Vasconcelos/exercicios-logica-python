def aumentar(a = 0,p = 0,formatado = False):
    """
        :param a: É substituido pelo preço
        :param p: Porcentagem
        :param formatado: formata o valor passado com cifrão, vírgula e casas decimais a direita caso verdadeiro.
    """
    resultado_porcentagem = a + (a * p/100)
    return resultado_porcentagem if formatado is False else moeda(resultado_porcentagem) #Solução do professor Gustavo Guanabara


def diminuir(a  = 0,p = 0,formatado = False):
    """
        :param a: É substituido pelo preço
        :param p: Porcentagem
        :param formatado: formata o valor passado com cifrão, vírgula e casas decimais a direita caso verdadeiro.
    """
    resultado_porcentagem = a - (a * p/100)
    if formatado: #Minha solução
        return moeda(resultado_porcentagem)
    else:
        return resultado_porcentagem


def dobro(a = 0,formatado = False):
    """
        :param a: É substituido pelo preço
        :param formatado: formata o valor passado com cifrão, vírgula e casas decimais a direita caso verdadeiro.
    """
    res = a*2
    if formatado:
        return moeda(res)
    else:
        return res


def metade(a = 0,formatado = False):
    """
        :param a: É substituido pelo preço
        :param formatado: formata o valor passado com cifrão, vírgula e casas decimais a direita caso verdadeiro.
    """
    res = a/2
    if formatado:
        return moeda(res)
    else:
        return res
    

def moeda(a = 0, moeda = 'R$'):
    return f'{moeda}{a:>2.2f}'.replace('.',',')

