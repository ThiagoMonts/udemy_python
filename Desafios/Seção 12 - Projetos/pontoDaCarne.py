# Desafio com If, Elif e Else

'''
Criar um programa que dependendo da temperatura (em celsius) do steak ele retorna o ponto de cozimento em português. O usuário deverá fornecer a temperatura.

Temperaturas - Cozimento
120ºF ou 48ºC - Rare (Selada)
130ºF ou 54ºC - Medium Rare (Ao ponto para Mal Passada)
140ºF ou 60ºC - Medium (Ao Ponto)
150ºF ou 66ºC - Medium Well (Ao Ponto para Bem Passada)
160ºF ou 71ºC - Well Done (Bem Passada)

> de 48ºC - Cozinhar por mais alguns minutos
< de 71ºC - Cuidado para não ter uma carne seca
'''


temperatura = int(input("Qual a temperatura da carne? Em graus Celsius: "))

if temperatura < 48:
    print("Cozinhar por mais alguns minutos")
elif 48 <= temperatura < 54:
    print("Rare (Selada)")
elif 54 <= temperatura < 60:
    print("Medium Rare (Ao ponto para Mal Passada)")
elif 60 <= temperatura < 66:
    print("Medium (Ao Ponto)")
elif 66 <= temperatura < 71:
    print("Medium Well (Ao Ponto para Bem Passada)")
else:
    print("Well Done (Bem Passada)")
    print("Cuidado para não ter uma carne seca")
