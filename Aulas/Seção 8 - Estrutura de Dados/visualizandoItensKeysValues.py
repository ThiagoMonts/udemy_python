
# Dicionários
    # Utiliza index no formato de Keys e Values (chave:valor)
    # Aceita string, integer, float, boolean...

aluno = {
    'nome': 'Ana',
    'idade': 16,
    'nota_final': 'A',
    'aprovação': True, 
    'Materias': ['Física','Matemática', 'Inglês']
}

print(aluno)
print(aluno.get('Materias'))
print(len(aluno))
print(aluno.keys())
print(aluno.items())
print(aluno.values())