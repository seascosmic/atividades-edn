'''4 - Crie um programa que realize consultas a cotações de moedas em relação ao Real (BRL) usando a API AwesomeAPI, 
mostre valor atual, máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, 
retorne uma mensagem de erro.  
'''

import requests

def consultar_moeda():
    moeda = input("Digite o código da moeda (ex: USD, EUR, BTC): ").strip().upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()

        dados = resposta.json()

        chave = f"{moeda}BRL"
        if chave not in dados:
            print("Moeda não encontrada.")
            return

        info = dados[chave]
        valor_atual = float(info["bid"])
        valor_maximo = float(info["high"])
        valor_minimo = float(info["low"])
        data_hora = info["create_date"]

        print("\n--- Cotação da Moeda ---")
        print(f"Moeda: {moeda}/BRL")
        print(f"Valor Atual: R$ {valor_atual:.2f}")
        print(f"Máximo: R$ {valor_maximo:.2f}")
        print(f"Mínimo: R$ {valor_minimo:.2f}")
        print(f"Última Atualização: {data_hora}")

    except requests.exceptions.RequestException:
        print("Falha na requisição. Verifique sua conexão com a internet.")

while True:
    consultar_moeda()

    repetir = input("\nDeseja consultar outra moeda? (s/n): ").strip().lower()
    if repetir != 's':
        print("Encerrando o programa. Até mais!")
        break
