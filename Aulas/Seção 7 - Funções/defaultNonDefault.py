
#Functions (Funções)
    # DRY - Don't Repeat Yourself.
    # Parâmetro --> Argumento
    # Default = Aquele que você define o valor no parâmetro
    # Non-Default = Aquele que você NÃO define o valor no parâmetro

    # Regra: O argumento default deve ser o último parâmetro da função, se você tiver mais de um parâmetro, os primeiros devem ser non-default e o último deve ser default. Do contrário, ocorrerá um erro. (Colocar o default no início e o non-default no final, não funciona)

def boas_vindas(nome, quantidade=6):
    print(f'Olá, {nome}!')
    print(f'Temos {str(quantidade)} laptops em estoque')


boas_vindas("Thiago", 5)