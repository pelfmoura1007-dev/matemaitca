from time import sleep

# Entrada de dados
alt = float(input("Digite a sua altura em metros (ex: 1.75): "))
peso = float(input("Digite o seu peso em kg (ex: 70.5): "))

# Processamento
imc = peso / (alt**2)

print(f"\nSeu IMC é {imc:.2f}. Analisando seus dados...")
sleep(2)

# Classificação
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc <= 24.9:
    print("Classificação: Peso ideal")
elif imc <= 29.9:
    print("Classificação: Sobrepeso")
elif imc <= 40.0:
    print("Classificação: Obesidade")
else:
    print("Classificação: Obesidade mórbida")