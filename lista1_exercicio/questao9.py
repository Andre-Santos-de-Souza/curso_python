# Problema "medidas"

medida_a = input('Digite a medida A: ')
medida_b = input('Digite a medida B: ')
medida_c = input('Digite a medida C: ')

area_quadrado = (float(medida_a)**2)
area_triangulo = (float(medida_a) * float(medida_b))/2
area_trapezio = ((float(medida_a)+float(medida_b))*float(medida_c))/2

print(f'AREA DO QUADRADO = {area_quadrado:.4f}')
print(f'AREA DO TRIANGULO = {area_triangulo:.4f}')
print(f'AREA DO TRAPEZIO = {area_trapezio:.4f}')