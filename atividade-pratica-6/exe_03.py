''''3 - Crie um programa que consulte informações de um CEP na API ViaCEP, 
retorne logradouro, bairro, cidade e estado do CEP digitado, caso o CEP não existir ou houver erro na requisição, 
mostre uma mensagem de falha'''


import requests

def consultar_cep():
    cep = input("Digite o CEP (somente números): ").strip()

    if len(cep) != 8 or not cep.isdigit():
        print("CEP inválido. Digite 8 números.")
        return

    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  

        dados = resposta.json()

        if "erro" in dados:
            print("CEP não encontrado.")
            return

        logradouro = dados.get("logradouro", "Não informado")
        bairro = dados.get("bairro", "Não informado")
        cidade = dados.get("localidade", "Não informado")
        estado = dados.get("uf", "Não informado")

        print("\n--- Informações do CEP ---")
        print(f"Logradouro: {logradouro}")
        print(f"Bairro: {bairro}")
        print(f"Cidade: {cidade}")
        print(f"Estado: {estado}")

    except requests.exceptions.RequestException:
        print("Falha na requisição. Verifique sua conexão com a internet.")

while True:
    consultar_cep()
    
    repetir = input("\nDeseja consultar outro CEP? (s/n): ").strip().lower()
    if repetir != 's':
        print("Encerrando o programa. Até mais!")
        break
