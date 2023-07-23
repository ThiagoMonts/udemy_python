
#Functions (Funções)
    # DRY - Don't Repeat Yourself.
    # Vários Argumentos (xargs) identificando o parâmetro

# Criar uma função que armazena números e strings (dados)


def agencia(**carro):
    return carro


print(agencia(marca='Gol', cor='Branca', motor=1.0, placa=1234))
print(agencia(marca='Gol', cor='Azul', motor=1.0))
print(agencia(marca='Gol', cor='Preto'))