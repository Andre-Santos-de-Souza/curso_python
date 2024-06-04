# Problema "dardo"

print('Digite as tres distancias:')

try:
    distancia_1 = input("Digite a distância 1: ")
    distancia_2 = input("Digite a distância 2: ")
    distancia_3 = input("Digite a distância 3: ")

    distancia_1 = float(distancia_1)
    distancia_2 = float(distancia_2)
    distancia_3 = float(distancia_3)

    # Verificação de qual distância é a maior
    if distancia_1 > distancia_2 and distancia_1 > distancia_3:
        print(f'MAIOR DISTANCIA = {distancia_1:.2f}')
    elif distancia_2 > distancia_1 and distancia_2 > distancia_3:
        print(f'MAIOR DISTANCIA = {distancia_2:.2f}')
    elif distancia_3 > distancia_1 and distancia_3 > distancia_1:
        print(f'MAIOR DISTANCIA = {distancia_3:.2f}')
    else:
        print(f'MAIOR DISTANCIA = {distancia_1:.2f}')
except ValueError:
    print('[ERROR]: Digite apenas números.')
