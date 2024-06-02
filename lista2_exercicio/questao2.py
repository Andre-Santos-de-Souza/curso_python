# Problema "baskara"
import math

coeficiente_a = input('Coeficiente a: ')
coeficiente_b = input('Coeficiente b: ')
coeficiente_c = input('Coeficiente c: ')

delta = (float(coeficiente_b)*float(coeficiente_b)) - 4*float(coeficiente_a)*float(coeficiente_c)

if delta < 0:
    print('Esta equacao nao possui raizes reais')
else:
    x1 = (-float(coeficiente_b) + math.sqrt(delta))/(2.0*float(coeficiente_a))

    x2 = (-float(coeficiente_b) - math.sqrt(delta))/(2.0*float(coeficiente_a))
    print(f'X1 = {x1:.4f}')
    print(f'X2 = {x2:.4f}')