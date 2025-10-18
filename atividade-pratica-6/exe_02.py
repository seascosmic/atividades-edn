'''Crie um programa que acesse a API Random User Generator para buscar um usuário fictício aleatório. 
exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha'''

import requests

def buscar_usuario():
    url = "https://randomuser.me/api/"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status() 

        dados = resposta.json()
        usuario = dados["results"][0]

        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario["email"]
        pais = usuario["location"]["country"]

        print("\n--- Usuário Aleatório Gerado ---")
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")

    except requests.exceptions.RequestException:
        print("\nFalha ao conectar à API. Verifique sua conexão com a internet.")

while True:
    buscar_usuario()

    repetir = input("\nDeseja buscar outro usuário? (s/n): ").strip().lower()
    if repetir != 's':
        print("Encerrando o programa. Até logo!")
        break
