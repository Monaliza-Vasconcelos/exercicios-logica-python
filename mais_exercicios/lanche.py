# Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

# Entrada
#O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

#Saída
#O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.


codigo = int(input())
quant_de_itens = int(input())
if codigo == 1:
    valor_a_pagar = (quant_de_itens * 4.00)
    print(f'Total: R$ {valor_a_pagar:.2f}')
elif codigo == 2:
    valor_a_pagar = (quant_de_itens *4.50)
    print(f'Total: R$ {valor_a_pagar:.2f}')
elif codigo == 3:
    valor_a_pagar = (quant_de_itens * 5.00)
    print(f'Total: R$ {valor_a_pagar:.2f}')
elif codigo == 4:
    valor_a_pagar = (quant_de_itens * 2.00)
    print(f'Total: R$ {valor_a_pagar:.2f}')
else:
    valor_a_pagar = (quant_de_itens * 1.50)
    print(f'Total: R$ {valor_a_pagar:.2f}')