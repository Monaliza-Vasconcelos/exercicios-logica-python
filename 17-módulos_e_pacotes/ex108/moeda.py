def aumentar(a = 0,p = 0):
    """
        :param a: É substituido pelo preço
        :param p: Porcentagem
        :return: Retorna o resultado do cálculo de porcentagem somado ao valor do preço
    """
    resultado_porcentagem = a + (a * p/100)
    return resultado_porcentagem


def diminuir(a  = 0,p = 0):
    """
        :param a: É substituido pelo preço
        :param p: Porcentagem
        :return: Retorna o resultado do cálculo de porcentagem subtraido ao valor do preço
    """
    resultado_porcentagem = a - (a * p/100)
    return resultado_porcentagem


def dobro(a = 0):
    """
        :param a: É substituido pelo preço
        :param p: Porcentagem
        :return: Retorna o resultado do cálculo  do dobro
    """
    res = a*2
    return res


def metade(a = 0):
    """
        :param a: É substituido pelo preço
        :param p: Valor da porcentagem passada
        :return: Retorna a divisão do preço por 2
    """
    res = a/2
    return res

def moeda(a = 0, moeda = 'R$'):
    return f'{moeda}{a:>2.2f}'.replace('.',',')

