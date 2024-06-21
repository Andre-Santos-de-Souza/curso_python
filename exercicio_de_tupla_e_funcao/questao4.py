from collections import Counter

def contar_elemento(tupla):
    contador = Counter(tupla)
    return contador.most_common(1)

tupla = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
funcao = contar_elemento(tupla)
print(f'O elemento que mais se repete é {funcao[0][0]}')