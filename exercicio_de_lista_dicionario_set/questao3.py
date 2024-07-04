
soma = []
def soma_indices_impares(lista):
    for i, lis in enumerate(lista):
        if i % 2 != 0:
            soma.append(lis)
    return sum(soma)

lista = [1, 2, 3, 4, 5, 6]
funcao = soma_indices_impares(lista)
print(funcao)