
# Lambda function
    # É uma função (pequena) sem nome
    # Pode ter vários argumentos, mas somente uma expressão
    # Muito utilizada dentro de outras funções
    # Código mais limpo e fácil de ler

# def somar(x):
#     return x + 10

# print(somar(2))

#Você digita lambda, os argumentos, depois ':' e a expressão
somar10 = lambda x: x + 10
print(somar10(2))

somar10 = lambda x,y: x + y + 10
print(somar10(2, 4))

