palavras = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar','trabalhar','mercado','programador','futuro')
for p in palavras:
    print(f'\nNa palavra {p} tem: ',end='')
    for C in p:
        if C in 'aeiou':
            print(f'{C}',end=' ')



