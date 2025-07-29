from random import choice
from time import sleep
print('PEDRA - PAPEL - TESOURA')
computador = ['pedra','papel','tesoura']
aleatorio = choice(computador)
Res_usuario = str(input('Deseja escolher qual opção? ')).lower().strip()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
if (aleatorio == 'pedra') and (Res_usuario == 'papel'):
    print('Usuário venceu')
elif (aleatorio == 'pedra') and (Res_usuario == 'tesoura'):
    print('Computador venceu')
elif (aleatorio == 'papel') and (Res_usuario == 'pedra'):
    print('Usuário venceu')
elif (aleatorio == 'papel') and (Res_usuario == 'tesoura'):
    print('Computador venceu')
elif (aleatorio == 'tesoura') and (Res_usuario == 'pedra'):
    print('Usuário venceu')
elif (aleatorio == 'tesoura') and (Res_usuario == 'papel'):
    print('Computador venceu')
else:
    print('Ninguém venceu')
print('Resposta do usuário: {}'.format(Res_usuario))
print('Resposta do computador: {}'.format(aleatorio))
print('FIM DE JOGO')
    


