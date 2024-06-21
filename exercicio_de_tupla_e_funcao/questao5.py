def obter_idades(tupla):
    nomes = []
    idades = []
    for nome,idade in tupla:
        nomes.append(nome)
        idades.append(idade)
    return idades

tupla_dados = (("João", 25), ("Maria", 30), ("Ana", 22))
funcao = obter_idades(tupla_dados)
print(funcao)