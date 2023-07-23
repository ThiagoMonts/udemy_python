
# === for loop nested ===

    # Outer loop
     # Inner loop

'''
Criar um retangulo de 6x6
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
'''

linhas = 6
colunas = 6
simbolo = '@'

for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end='')
    print() # A outer loop pulará para a proxima linha, quando fizer o loop