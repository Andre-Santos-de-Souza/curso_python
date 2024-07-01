def contar_ocorrencias(lista, valor):
    contagem = 0
    for item in lista:
        if item == valor:
            contagem += 1
    return contagem

numeros = [1, 2, 2, 3, 4, 4, 4]
print(contar_ocorrencias(numeros, 4))