s = float(input())
if (s>=0) and (s<=400):
    porcentagem = (s*15)/100
    percentual = 15
elif (s>400) and (s<=800):  
    porcentagem = (s*12)/100
    percentual = 12
elif (s>800) and (s<=1200):
    porcentagem = (s*10)/100
    percentual = 10
elif (s>1200) and (s<=2000):
    porcentagem = (s*7)/100
    percentual = 7
else:
    porcentagem = (s*4)/100
    percentual = 4
novo_salario = s + porcentagem
print(f"Novo salário: {novo_salario:.2f}")
print(f"Reajuste ganho: {porcentagem:.2f}")
print(f'Em percentual: {percentual} %')


