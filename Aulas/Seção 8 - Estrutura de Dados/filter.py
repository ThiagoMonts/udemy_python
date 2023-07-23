
# Filter Function1
    # Muito utilizado com listas
    # Aplicar uma função a um Iterable, filtrando os itens. (list, tuple, dict, etc)

valores = [10, 12, 34, 44, 57]

# def remover20(x):
#     return x > 20

# print(list(filter(remover20, valores)))

print(list(filter(lambda x: x > 20, valores))) #Com a função lambda