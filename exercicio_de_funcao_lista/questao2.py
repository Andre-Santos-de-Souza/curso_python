def multiplica_lista(numeros):
    n = 1
    for num in numeros:
        n *= num
    return n

lista = [1,2,3,4,5]
funcao = multiplica_lista(lista)
print(funcao)