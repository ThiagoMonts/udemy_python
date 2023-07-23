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
    
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome
        

# Criar o objeto
usuario1 = Funcionarios('Elena', 'Cabral', '12/01/2009')
usuario2 = Funcionarios('Carol', 'Silva', '15/10/2005')
usuario3 = Funcionarios('André', 'Iacono', '11/03/2003')

# Print 
# print(usuario1.nome + ' ' + usuario1.sobrenome)
print(usuario1.nome_completo())
print(Funcionarios.nome_completo(usuario1))
