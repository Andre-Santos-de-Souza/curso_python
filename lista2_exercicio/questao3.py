# Problema "menor_de_tres"

try:

    primeiro_valor = input('Primeiro valor: ')
    segundo_valor = input('Segundo valor: ')
    terceiro_valor = input('Terceiro valor: ')

    valor_1 = int(primeiro_valor)
    valor_2 = int(segundo_valor)
    valor_3 = int(terceiro_valor)

    if valor_1 < valor_2 and valor_1 < valor_3:
        print(f'MENOR = {valor_1}')
    elif valor_2 < valor_1 and valor_2 < valor_3:
        print(f'MENOR = {valor_2}')
    elif valor_3 < valor_1 and valor_3 < valor_2:
        print(f'MENOR = {valor_3}')
    elif valor_1 == valor_2 and valor_1 == valor_3:
        print(f'MENOR = {valor_1}')
    elif valor_1 == valor_2 and valor_1 < valor_3:
        print(f'MENOR = {valor_1}')
    elif valor_1 < valor_2 and valor_1 == valor_3:
        print(f'MENOR = {valor_1}')
    elif valor_2 < valor_1 and valor_2 == valor_3:
        print(f'MENOR = {valor_2}')
    else:
        print('[ERROR]:  Algo inesperado aconteceu.')

except ValueError:
    print('[ERROR]: Digite apenas números inteiros.')
