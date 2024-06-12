# Problema "media_idades"

while True:
    print('Digite as idades')
    idade_1 = input('Digite sua idade: ')
    idade_2 = input('Digite sua idade: ')
    idade_3 = input('Digite sua idade: ')
    idade_4 = input('Digite sua idade: ')

    idade_1 = int(idade_1)
    idade_2 = int(idade_2)
    idade_3 = int(idade_3)
    idade_4 = int(idade_4)

    if idade_1 > 0:
        media = (idade_1 + idade_2 + idade_3 + idade_4)/4
        print(f'MEDIA = {media:.2f}')
    elif idade_1 < 0:
        print('IMPOSSIVEL CALCULAR')
        break