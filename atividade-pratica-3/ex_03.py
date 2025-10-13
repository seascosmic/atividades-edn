### 3- Conversor de Temperatura Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
# O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

temperatura = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C, F ou K): ").upper()
destino = input("Digite a unidade de destino (C, F ou K): ").upper()

if origem == "C":
    temp_c = temperatura
elif origem == "F":
    temp_c = (temperatura - 32) * 5/9
elif origem == "K":
    temp_c = temperatura - 273.15
else:
    print("Unidade de origem inválida!")
    exit()

if destino == "C":
    resultado = temp_c
elif destino == "F":
    resultado = (temp_c * 9/5) + 32
elif destino == "K":
    resultado = temp_c + 273.15
else:
    print("Unidade de destino inválida!")
    exit()

print(f"\n{temperatura:.2f}°{origem} equivalem a {resultado:.2f}°{destino}")
