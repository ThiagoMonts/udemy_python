# Desafio com Funções

'''
Criar um programa que calcula a quantidade de tinta necessária para pintar um parede. O usuário deverá fornecer as seguintes informações: Rendimento, altura e largura.
O programa deve mostrar na tela a mensagem: "Você necessita de X latas de tinta."
'''

rendimento = int(input("Qual é o rendimento da lata? Em m² por litro: "))
altura = int(input("Qual é a altura da parede? Em metros: "))
largura = int(input("Qual é a largura da parede? Em metros: "))

def calculoTinta(rendimento, altura, largura):
    area = altura * largura
    total = area / rendimento
    return total


print(f'Você necessita de {calculoTinta(rendimento, altura, largura)} latas de tinta.')