
# Sets (Listas)
    # Similar a listas
    # Evita itens duplicados
    # Não utiliza index

list1 = [1, 2, 3, 4, 5, 6]
s1 = {1, 2, 3, 5, 6}
#s1.add(7) # Adiciona um item ao set
#s1.update([8, 9, 10]) # Adiciona vários itens ao set
#s1.remove(10) # Remove um item do set (gera um erro se o item não existir no set)
s1.discard(10) # Remove um item do set, mas não dá erro se o item não existir

#print(list1)
print(s1)
#print(type(list1))
#print(type(s1))