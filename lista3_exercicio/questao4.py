# Problema "quadrante"

while True:
    try:
        print('Digite os valores das coordenadas X e Y:')
        coordenada_x = int(input('Digite o valor da coordenada X : '))
        coordenada_y = int(input('Digite o valor da coordenada Y : '))

        if coordenada_x > 0 and coordenada_y > 0:
            print('QUADRANTE Q1')
        elif coordenada_x > 0 and coordenada_y < 0:
            print('QUADRANTE Q4')
        elif coordenada_x < 0 and coordenada_y < 0:
            print('QUADRANTE Q3')
        elif coordenada_x < 0 and coordenada_y > 0:
            print('QUADRANTE Q2')
        else:
            break
    except:
        print("Digite apenas números inteiros.")