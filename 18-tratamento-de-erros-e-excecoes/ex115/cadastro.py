import json
def menu(resposta):
    """
        :param resposta: joga a informação de escolha opção do programa principal para a função
        e cria um input onde pergunta o usuário a opção
        :return Sair: Retorna ao programa principal e finaliza o loop do while
    """
    print('-'*50)
    print('MENU PRINCIPAL'.center(50))
    print('-'*50)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova Pessoa')
    print('3 - Sair do Sistema')
    print('-'*50)
    try:
        resp = input(resposta)
        if resp == '1':
            pessoas_cadastradas()
        elif resp == '2':
            cadastro_de_pessoas()
        elif resp == '3':
            return 'Sair'
        else:
            print('\033[0;31mOpção inválida\033[m')
    except KeyboardInterrupt:
        print('\033[0;31mO usuário decidiu encerrar o programa\033[m')
        return 'Sair'


def pessoas_cadastradas():
    print('-'*50)
    print('PESSOAS CADASTRADAS'.center(50))
    print('-'*50)
    #Lendo o arquivo json e mostrando o conteúdo
    try:
        with open("meucadastro.json", "r", encoding="utf-8") as arquivo:
            lista = json.load(arquivo)
            for pessoa in lista:
                print(f'\033[0;34m{pessoa["Nome"]:<40}{pessoa["Idade"]} anos\033[m')
    except (FileNotFoundError,json.JSONDecodeError):
        lista = []
        print('\033[0;31mSem dados cadastrados\033[m')



def cadastro_de_pessoas():
    while True:
        try:
            nome = str(input('Nome: '))
            idade = int(input('Idade: '))
            break
        except (ValueError,TypeError):
            print('\033[0;31mOpção inválida\033[m')
        except nome == '':
            print('\033[0;31mOpção inválida\033[m')
    dados = {"Nome":nome,
              "Idade":idade}
    try:
        with open("meucadastro.json","r",encoding="utf-8") as arquivo:
            lista = json.load(arquivo)
          
    except (FileNotFoundError,json.JSONDecodeError):
        lista = []


    lista.append(dados)
#Adicionando os dados ao arquivo json
    with open("meucadastro.json","w",encoding="utf-8") as arquivo:
        json.dump(lista,arquivo,indent=4)
        print('\033[0;33mAdicionado com sucesso.\033[m')
            


   



    
    







        