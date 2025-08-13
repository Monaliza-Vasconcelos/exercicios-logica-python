def ficha(j=0,g=0):
    """
        -> Ficha onde é mostrado o nome e gols realizados de um jogador
        :param j: Retorna o nome do jogador se informado, caso não seja, retorna desconhecido
        :param g: Retorna a quantidade de gols, se não digitado nada, retorna 0
    """
    if j in '' and g not in '':
        return(f'O jogador <desconhecido> fez {g} gol(s) no campeonato.')
    elif g in '' and j not in '':
        return(f'O jogador {j} fez {g} gol(s) no campeonato.')
    elif g in '' and j in '':
        return(f'O jogador <desconhecido> fez 0 gol(s) no campeonato.')
    else:
        return(f'O jogador {j} fez {g} gol(s) no campeonato.')

#programaprincipal
R1 = str(input('Nome do jogador: '))
R2 = (input('Número de Gols: '))
print(ficha(R1,R2))
