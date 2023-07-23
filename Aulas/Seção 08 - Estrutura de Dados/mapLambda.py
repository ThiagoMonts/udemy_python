
# Map Function
    # Muito utilizado com listas
    # Aplicar uma função a um Iterable, por item. (list, tuple, dict, etc)

lista1 = [1, 2, 3, 4]

# def multi(x):
#     return x * 2

# print(multi(2))

#lista2 = map(lambda x: x * 2, lista1)

print(list(map(lambda x: x * 2, lista1)))