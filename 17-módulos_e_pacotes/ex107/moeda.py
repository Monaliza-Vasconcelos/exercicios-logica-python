def aumentar(a,p):
    """
        :param a: É substituido pelo preço
        :param p: Porcentagem
        :return: Retorna o resultado do cálculo de porcentagem somado ao valor do preço
    """
    resultado_porcentagem = a + (a * p/100)
    return resultado_porcentagem


def diminuir(a,p):
    """
        :param a: É substituido pelo preço
        :param p: Porcentagem
        :return: Retorna a subtração do cálculo da porcentagem com o preço passado
    """
    resultado_porcentagem = a - (a * p/100)
    return resultado_porcentagem


def dobro(a):
    """
        :param a: É substituido pelo preço
        :return: Retorna a multiplicação do preço por 2
    """
    res = a*2
    return res


def metade(a):
    """
        :param a: É substituido pelo preço
        :return: Retorna a divisão do preço por 2
    """
    res = a/2
    return res
