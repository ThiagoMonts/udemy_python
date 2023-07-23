# Listas

    # Armazenar mais de uma informação em uma variável
    # Manter a sequência dos dados em uma variável

cores = ['amarelo', 'verde', 'azul', 'vermelho']
valores = [10, 20, 30, 40]

duas_listas = zip(cores, valores) #Agrega as listas, irá juntar o item 0 da lista cores, com o item 0 da lista valores, e assim por diante

print(list(duas_listas)) #Converte o zip em lista

# var = list('André') #Gera uma lista automaticamente, separando as letras
# print(var)