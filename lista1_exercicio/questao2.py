import math

base_retangulo = input('Base do retangulo: ')
altura_retangulo = input('Altura do retangulo: ')

area = float(base_retangulo) * float(altura_retangulo)

perimetro = (float(base_retangulo)+float(altura_retangulo))*2

diagonal = math.sqrt((float(base_retangulo)**2)+(float(altura_retangulo)**2))

print(f'AREA = {area:.4f}')
print(f'PERIMETRO = {perimetro:.4f}')
print(f'DIAGONAL = {diagonal:.4f}')