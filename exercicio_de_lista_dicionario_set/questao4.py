def produto_mais_caro(dicionario):
    return max(dicionario)

dicionario = {"apple": 2.5, "banana": 1.0, "cherry": 3.0}
funcao = produto_mais_caro(dicionario)
print(funcao)