# Problema "terreno"
largura_terreno = input("Digite a largura do terreno:  ")

comprimento_terreno = input("Digite o comprimento do terreno: ")

valor_metro_quadrado = input("Digite o valor do metro quadrado: ")

area_terreno = float(largura_terreno) * float(comprimento_terreno)

preco_terreno = float(valor_metro_quadrado) * float(area_terreno)

print(f'Area do terreno = {area_terreno:.2f}')
print(f'Preco do terreno = {preco_terreno:.2f}')