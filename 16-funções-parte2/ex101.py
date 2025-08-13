def voto(ano):
    from datetime import date
    R = 0
    R = date.today().year - ano
    if R < 18:
        return (f'Com {R} anos: Voto NEGADO')
    elif (R >= 18) or (R < 65):
        return (f'Com {R} anos: Voto OBRIGATÓRIO')
    else:
        return (f'Com {R} anos: Voto OPCIONAL')


#programaprincipal
print('-'*30)
Resp = int(input('Ano nascimento: '))
print(f'{voto(Resp)}')
