dicionario_invertido = {}
def inverter_dicionario(dicionario):
    for chave,valor in dicionario.items():
        dicionario_invertido[valor] = chave
    return dicionario_invertido

dicionario = {"a": 1, "b": 2, "c": 3}
funcao = inverter_dicionario(dicionario)
print(funcao)