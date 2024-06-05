# Problema "coordenadas"

try:
    valor_x = float(input('Valor de X: '))
    valor_y = float(input('Valor de Y: '))

    if valor_x > 0 and valor_y < 0:
        print('Q4')
    elif valor_x > 0 and valor_y > 0:
        print('Q1')
    elif valor_x < 0 and valor_y < 0:
        print('Q3')
    elif valor_x < 0 and valor_y > 0:
        print('Q2')
    elif valor_x == 0 and valor_y == 0:
        print('Origem')
    elif (valor_x > 0 and valor_y == 0) or (valor_x < 0 and valor_y == 0):
        print("Eixo X")
    else:
        print('Eixo Y')
except:
    print('Digite apenas números.')