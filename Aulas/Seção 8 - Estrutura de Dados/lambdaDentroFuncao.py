
# Lambda function
    # É uma função (pequena) sem nome
    # Pode ter vários argumentos, mas somente uma expressão
    # Muito utilizada dentro de outras funções
    # Código mais limpo e fácil de ler

def somar(x):
    func2 = lambda x: x + 10
    return func2(x) * 4

print(somar(2))