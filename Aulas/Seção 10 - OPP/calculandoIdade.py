from datetime import datetime
# Python Object-Oriented Programming

# Classes
    # Utilizadas para criar Objetos (instances)
    # Objetos são partes dentro de uma Class (instâncias)
    # Classes são utilizadas para agrupar dados e funções, podendo reutilizar

# Criar a classe
class Funcionarios:
    
    #Sempre começa com o init, pois se trata de um construtor
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento 
    
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome
    
    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(self.ano_nascimento)  # Convertendo para inteiro
        return ano_atual - self.ano_nascimento
        

# Criar o objeto
usuario1 = Funcionarios('Elena', 'Cabral', '2009')
usuario2 = Funcionarios('Carol', 'Silva', '2005')
usuario3 = Funcionarios('André', 'Iacono', '2003')

# Print
print(Funcionarios.idade_funcionario(usuario1))
