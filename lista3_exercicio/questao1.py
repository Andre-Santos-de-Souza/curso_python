# Problema "crescente"

while True:
    x = int(input('Digite um número: '))
    y = int(input('Digite outro número: '))

    if x > y:
        print('DECRESCENTE!')
    elif x < y:
        print('CRESCENTE!')
    elif x == y:
        break