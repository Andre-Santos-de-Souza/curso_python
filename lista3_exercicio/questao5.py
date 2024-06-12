# Problema "validacao_de_nota"

nota_1 = float(input('Digite a primeira nota: '))
while nota_1 < 0 or nota_1 > 10:
    nota_1 = float(input("Valor invalido! Tente novamente: "))

nota_2 = float(input('Digite a segunda nota: '))
while nota_2 < 0 or nota_2 > 10:
    nota_2 = float(input("Valor invalido! Tente novamente: "))

media = (nota_1+nota_2)/2
print(f'MEDIA = {media:.2f}')