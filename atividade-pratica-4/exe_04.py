# 4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.

numeros = []
pares = 0
impares = 0

while True:
    entrada = input("Digite um número (ou 'sair' para encerrar): ")
    if entrada.lower() == 'sair':
        break
    try:
        numero = int(entrada)
        numeros.append(numero)
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    except ValueError:
        print("Por favor, digite um número válido.")

print(f"Números digitados: {numeros}")
print(f"Total de pares: {pares}")
print(f"Total de ímpares: {impares}")