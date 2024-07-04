lista_pares = []
def filtrar_pares(lista):
    for lis in lista:
        if lis % 2 == 0:
            lista_pares.append(lis)
    return lista_pares

lista = [1,2,3,4,5,6]
funcao = filtrar_pares(lista)
print(funcao)