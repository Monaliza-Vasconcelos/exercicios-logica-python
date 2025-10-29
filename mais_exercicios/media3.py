r1,r2,r3,r4 = map(float,input().split())
n1 = r1*2
n2 = r2*3
n3 = r3*4
n4 = r4*1
soma_produto = n1+n2+n3+n4
media_ponderada = soma_produto/10
if media_ponderada >= 7:
    print(f"Media: {media_ponderada:.1f}")
    print("Aluno aprovado.")
elif media_ponderada < 5:
    print(f"Media: {media_ponderada:.1f}")
    print("Aluno reprovado.")
elif (media_ponderada >= 5) and (media_ponderada < 6.9):
    nota_exame = float(input())
    media = (nota_exame + media_ponderada)/2
    print(f"Media: {media_ponderada:.1f}")
    print("Aluno em exame.")
    if media >= 5:
        print(f"Nota do exame: {nota_exame:.1f}")
        print("Aluno aprovado.")
        print(f"Media: {media:.1f}") 
    elif media <= 4.9:
        print(f"Nota do exame: {nota_exame:.1f}")
        print("Aluno reprovado.")
        print(f"Media: {media:.1f}")
        
    
    