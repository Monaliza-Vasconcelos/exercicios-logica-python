def notas(*n,sit=False):
    """
        -> Lista de notas da turma
        :param n: Recebe as notas dos alunos
        :param sit: Opcional e passa a situação da turma
        :return n: retorna a maior nota, a menor, a média e o total de notas passadas dentro de um
    """
    lista = {}
    print('-'*60)
    lista['total'] = len(n)
    lista['maior'] = max(n)
    lista['menor'] = min(n)
    lista['media'] = sum(n)/len(n)
    #Verificando a situação da turma
    if sit:
        if lista['media'] >= 7:
            lista['situação'] = 'Boa'
        elif lista['media'] < 7 and lista['media'] >= 6:
            lista['situação'] = 'Razoável'
        else:
            lista['situação'] = 'Ruim'
    return lista

#programa principal
resp = notas(6.5,7,4,6.5,2,7,4,sit=True)
print(resp)