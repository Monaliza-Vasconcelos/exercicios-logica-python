import requests


try:

    url = requests.get("https://www.pudim.com.br")
    print('Site pudim está ativo')
except:
    print('Erro')