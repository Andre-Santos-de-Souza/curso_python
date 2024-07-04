
lista = []
def dicionario_para_tuplas(dicionario):
    for chave,valor in dicionario.items():
        chave_valor = chave,valor
        lista.append(tuple(chave_valor))
    return lista

dicionario = {"a": 1, "b": 2, "c": 3}
funcao = dicionario_para_tuplas(dicionario)
print(funcao)
