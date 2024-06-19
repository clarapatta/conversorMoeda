import requests

def pegar_cotaçao_moeda(moeda_origem, moeda_destino):
    link = f"https://economia.awesomeapi.com.br/last/{moeda_origem}-{moeda_destino}"
    requisição = requests.get(link)
    
    cotaçao = requisição.json()[f"{moeda_origem}{moeda_destino}"]["bid"]
    return cotaçao
