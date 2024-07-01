def calcular_media(lista):
    if lista == []:
        return 'Lista vazia'
    else:
        return sum(lista) / len(lista)

lista_exemplo = []
media = calcular_media(lista_exemplo)
print(f"Média dos elementos: {media}")