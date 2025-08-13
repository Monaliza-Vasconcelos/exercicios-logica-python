def fatorial(n,show=False):
    """
        ->Calculando o fatorial de um número
        :param n: Recebe o valor passado para realizar o calculo
        :param show: é um valor opcional que por padrão é False
        :return: Retorna o fatorial de n
    """
    f = 1
    if show == True:
        for c in range(n,0,-1):
            f *= c
            if c > 1:
                print(f'{c}',end=' X ')
            else:
                print(f'{c}',end=' = ')
                
        return f
    else:
        for c in range(n,0,-1):
            f = c*f
        return f


print(fatorial(5,True))