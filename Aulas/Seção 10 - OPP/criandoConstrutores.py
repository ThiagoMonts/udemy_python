# Python Object-Oriented Programming

# Classes
    # Utilizadas para criar Objetos (instances)
    # Objetos são partes dentro de uma Class (instâncias)
    # Classes são utilizadas para agrupar dados e funções, podendo reutilizar

# Criar a classe
class Funcionarios:
    
    #Sempre começa com o init, pois se trata de um construtor
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento 
        

# Criar o objeto
usuario1 = Funcionarios('Elena', 'Cabral', '12/01/2009')
usuario2 = Funcionarios('Carol', 'Silva', '15/10/2005')
usuario3 = Funcionarios('André', 'Iacono', '11/03/2003')

# Print 
print(usuario1.nome)
print(usuario2.data_nascimento)
print(usuario3.sobrenome)

# # Criar os parâmetros do usuário 1
# usuario1.nome = 'Elena'
# usuario1.sobrenome = 'Cabral'
# usuario1.data_nascimento = '12/01/2009'

# # Criar os parâmetros do usuário 2
# usuario2.nome = 'Carol'
# usuario2.sobrenome = 'Silva'
# usuario2.data_nascimento = '15/10/2005'

