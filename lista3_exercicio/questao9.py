# Problema "soma_impares"

valor_x = int(input('Digite um número: '))
valor_y = int(input('Digite outro número: '))

soma = 0
if valor_x < valor_y:
    for i in range(valor_x+1, valor_y):
            if i % 2 != 0:
                soma += i
    
if valor_x > valor_y:
    for i in range(valor_y+1, valor_x):
        if i % 2 != 0:
            soma += i

print(f'SOMA DOS IMPARES = {soma}')