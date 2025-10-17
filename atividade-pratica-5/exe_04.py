# 4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.
from datetime import datetime
def calcular_dias_vivo(data_nascimento: str) -> int:
    data_nascimento_dt = datetime.strptime(data_nascimento, "%d/%m/%Y")
    data_atual = datetime.now()
    dias_vivo = (data_atual - data_nascimento_dt).days
    return dias_vivo
while True:
    data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    try:
        dias_vivo = calcular_dias_vivo(data_nascimento)
        print(f"Você está vivo há {dias_vivo} dias.")
    except ValueError:
        print("Data inválida. Por favor, use o formato dd/mm/aaaa.")
        continue

    repetir = input("Deseja calcular novamente? (s/n): ").strip().lower()
    if repetir != 's':
        print("Encerrando o programa. Até mais!")
        break
    