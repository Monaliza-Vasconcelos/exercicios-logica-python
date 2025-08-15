import moeda


escolha_usuario = float(input('Digite o preço R$'))
print(f'A metade de {escolha_usuario} é {moeda.metade(escolha_usuario)}')
print(f'O dobro de {escolha_usuario} é {moeda.dobro(escolha_usuario)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(escolha_usuario,10)}')
print(f'Diminuindo em 13%,  temos R${moeda.diminuir(escolha_usuario,13)}')


