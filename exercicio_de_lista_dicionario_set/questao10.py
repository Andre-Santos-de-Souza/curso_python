def contar_numeros(lista):
    chave_valor = {}
    chave = 1
    for valor in lista:
        if valor not in chave_valor.values():
            chave_valor[chave] = valor
            chave+=1
    return chave_valor

lista = [1, 2, 2, 3, 3, 3]
funcao = contar_numeros(lista)
print(funcao)