# Unpacking Listas

    # Armazenar mais de uma informação em uma variável
    # Manter a sequência dos dados em uma variável

produtos = ['arroz', 'feijão', 'laranja', 'banana', 5, 6, 7, 8]
#              0         1         2          3

item1, item2, item3, *outros = produtos

print(item1)
print(item2)
print(item3)
print(outros)