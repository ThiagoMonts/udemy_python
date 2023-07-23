
# Sets (Listas)
    # Similar a listas
    # Evita itens duplicados
    # Não utiliza index

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) # Union - Une as duas listas, tirando os itens repetidos
print(num1 - num2) # Difference - Mostra os itens que estão na lista 1 e não estão na lista 2
print(num1 ^ num2) # Symmetric Difference - Mostra os itens que estão nas duas listas, mas não em ambas
print(num1 & num2) # And - Mostra os itens que estão nas duas listas (interseção)

print(len(num1)) # Mostra o tamanho da lista