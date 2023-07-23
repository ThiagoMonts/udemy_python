
#Functions (Funções)
    # DRY - Don't Repeat Yourself.
    # Realizam uma tarefa
    # Calcula e retorna um Valor

def cliente1(nome):
    print(f'Olá, {nome}!')


def cliente2(nome):
    return f'Olá, {nome}!' # Retorna um valor


x = cliente1("Maria")
y = cliente2("José")

print(x)
print(y)

'''
Se você quer só executar uma tarefa, como por exemplo apenas exibir algo na tela, utiliza o print.

Se você vai reutilizar aquele dado depois, você usa o return, pois ele será  armazenado na memória e pode ser reutilizado futuramente.
'''