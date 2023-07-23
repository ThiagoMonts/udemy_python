
# Sets (Listas)
    # Similar a listas
    # Evita itens duplicados
    # Não utiliza index

set1 = {'a', 'b', 'c'}
set2 = {'a', 'b', 'e'}
set3 = {'c', 'd', 'f'}

#set4 = set1.union(set2) # Union - Une as duas listas, tirando os itens repetidos
#set4 = set1.difference(set3) # Difference - Mostra os itens que estão na lista 1 e não estão na lista 3
#set4 = set1.intersection(set2) # And - Mostra os itens que estão nas duas listas (interseção)

set4 = set1.symmetric_difference(set3) # Symmetric Difference - Mostra os itens que estão nas duas listas, mas não em ambas

print(set4)