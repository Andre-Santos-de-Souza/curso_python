# Problema "media_ponderada"

numero_de_casos_de_teste = int(input("Quantos casos voce vai digitar? "))
media = 0
for i in range(0, numero_de_casos_de_teste):
    num_1 = float(input("Digite o primeiro número: "))
    num_2 = float(input("Digite o segundo número: "))
    num_3 = float(input("Digite o terceiro número: "))

    media_ponderada = ((num_1*2)+(num_2*3)+(num_3*5))/10

    print(f"MEDIA = {media_ponderada:.1f}")
    