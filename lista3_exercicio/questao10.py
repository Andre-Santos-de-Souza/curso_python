# Problema "sequencia_impares"

valor_x = input("Digite o valor de X: ")
valor_x = int(valor_x)

for i in range(1, valor_x):
    if i % 2 != 0:
        print(i)