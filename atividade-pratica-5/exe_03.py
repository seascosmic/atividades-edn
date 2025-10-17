'''3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual. 
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem. 
b - Preço final: Determina o novo preço após o desconto. 
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos). 
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.'''


def calcular_desconto(preco: float, porcentagem_desconto: float) -> float:
    valor_desconto = preco * (porcentagem_desconto / 100)
    preco_final = preco - valor_desconto
    return round(preco_final, 2)


while True:
    print("\n--- Cálculo de Desconto ---")
    
    preco = float(input("Digite o preço do produto: R$ "))
    desconto = float(input("Digite a porcentagem de desconto (%): "))

    preco_final = calcular_desconto(preco, desconto)
    valor_desconto = preco - preco_final

    print(f"\nDesconto aplicado: R$ {valor_desconto:.2f}")
    print(f"Preço final com desconto: R$ {preco_final:.2f}")

    repetir = input("\nDeseja calcular outro desconto? (s/n): ").strip().lower()
    if repetir != 's':
        print("Encerrando o programa. Até logo!")
        break
