
# Dicionários
    # Utiliza index no formato de Keys e Values (chave:valor)
    # Aceita string, integer, float, boolean...

aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

#aluno['nome'] = 'José'
# aluno.update({'nome': 'José', 'nota_final': 'B'}) #Consigo atualizar mais de um valor ao mesmo tempo
# aluno.update({'endereço': 'Rua A'})
# print(aluno)

del aluno['idade'] #Deleta a key e o valor
print(aluno)
#print(aluno.get('endereço', 'Não existe')) #Não retorna erro caso a key não exista, além de poder colocar uma mensagem de erro