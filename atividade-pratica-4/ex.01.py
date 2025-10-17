# 1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).

num1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: divisão por zero não é permitida!")
        exit()
else:
    print("Operação inválida!")
    exit()

print(f"\nResultado: {num1} {operacao} {num2} = {resultado}")
