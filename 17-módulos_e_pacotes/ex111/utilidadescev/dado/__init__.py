def leiaDinheiro(f):
    while True:
        x = input(f).replace(',','.').strip()
        if x.isalpha() or x == '':
            print(f'\033[0;31mErro: "{x}" é inválido.\033[m')
        else:
            x = float(x)
            return x
            
            
        

