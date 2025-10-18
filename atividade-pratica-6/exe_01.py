'''  1 - Crie um programa que gere senhas aleatórias com letras, números e símbolos e que o usuário  
também escolha o tamanho da senha  para criar senhas seguras automaticamente.'''

import random
import string

def gerar_senha(tamanho: int) -> str:
    caracteres = string.ascii_letters + string.digits + string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

while True:
    print("\n--- GERADOR DE SENHAS SEGURAS ---")

    try:
        tamanho = int(input("Digite o tamanho desejado da senha: "))

        if tamanho < 6:
            print("A senha deve ter pelo menos 6 caracteres para ser segura.")
            continue

        senha = gerar_senha(tamanho)
        print(f"\n Senha gerada: {senha}")

    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    repetir = input("\nDeseja gerar outra senha? (s/n): ").strip().lower()
    if repetir != 's':
        print("Encerrando o programa. Até mais!")
        break
