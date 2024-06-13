# Problema "pares_consecutivos"

while True:
    soma = 0
    numero_int = int(input('Digite um numero inteiro: '))
    if numero_int == 0:
        break
    elif numero_int % 2 != 0:
        soma = (soma + numero_int)+1
        for i in range(1,5):
            numero_int += 2
            soma += numero_int+1
    elif numero_int % 2 == 0:
        soma += numero_int
        for i in range(4):
            numero_int += 2
            soma += numero_int
    print(f'SOMA = {soma}')