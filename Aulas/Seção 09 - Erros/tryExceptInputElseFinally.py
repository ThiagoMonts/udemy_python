# Erros
    # Excelente para testes
    # Não realiza o 'stop' no programa
    # Mensagens customizadas quando encontra um erro

try: 
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor numérico')
finally: # O finally sempre será executado, independente se o usuário digitar um valor correto ou não
    print('Código OK')


# else: # O else só será executado se o usuário digitar um valor correto
#     print('Usuário digitou um valor correto')
#     resultado = valor * 2
#     print(resultado)

print('mais código abaixo')