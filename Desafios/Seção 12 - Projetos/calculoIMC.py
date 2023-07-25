# Cálculo de IMC - Índice de Massa Corporal

'''
Qual é sua altura em cm:
Qual é seu peso em kg:

Menor que 18,5 - Abaixo do peso
Entre 18,5 e 24,9 - Peso normal
Entre 25 e 29,9 - Sobrepeso
Entre 30 e 34,9 - Obesidade grau 1
Entre 35 e 39,9 - Obesidade grau 2
Maior que 40 - Obesidade grau 3
'''

altura = float(input("Qual é sua altura em cm? "))
peso = float(input("Qual é seu peso em kg? "))

imc = peso / (altura/100)**2


if imc < 18.5:
    print(f"Seu IMC é {imc:.2f} - Abaixo do peso")
elif 18.5 >= imc < 24.9:
    print(f"Seu IMC é {imc:.2f} - Peso normal")
elif 24.9 >= imc < 29.9:
    print(f"Seu IMC é {imc:.2f} - Sobrepeso")
elif 29.9 >=imc < 34.9:
    print(f"Seu IMC é {imc:.2f} - Obesidade grau 1")
elif 34.9 >= imc < 39.9:
    print(f"Seu IMC é {imc:.2f} - Obesidade grau 2")
else:
    print(f"Seu IMC é {imc:.2f} - Obesidade grau 3")