"""
Exercício
Exiba os índices da lista
"""
lista = ["Maria","Helena","Luiz"]
lista.append('João')
indice = 0
for nome in lista:
    print(indice,nome, type(nome))
    indice += 1