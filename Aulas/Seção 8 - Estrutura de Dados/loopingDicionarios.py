
# Dicionários
    # Utiliza index no formato de Keys e Values (chave:valor)
    # Aceita string, integer, float, boolean...

aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

# for x in aluno:
#     print(x) #Retorna apenas as keys

# for x in aluno.values():
#     print(x) #Retorna os valores

for x in aluno.items():
    print(x) #Retorna as keys e os valores, mas em formato de tupla

for keys, values in aluno.items():
    print(keys, values) #Retorna as keys e os valores, tirando o formato de tupla

