soma = C = tot3 = 0
total = ( int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')))
print(f'Você digitou os valores {total}')
print(f'O valor 9 apareceu {total.count(9)} vezes')
print('Os valores pares digitados foram: ',end=' ')
for C in range(0,4):
    if (total[C]%2==0):
        print(total[C],end=' ')
    if total[C] == 3:
        tot3 += 1
print()
if tot3 != 0:
    print(f'O valor 3 apareceu na {total.index(3) + 1}º posição')
else:
    print('O valor 3 não apareceu em nenhuma posição')



       
