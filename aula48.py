"""
Listas em python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
     append - Adiciona um item ao final
     insert - Adiciona um item no índice escolhido
     pop - Remove do final ou do índice escolhido
     del - Apaga um índice
     clear - limpa a lista
     extend - estende a lista
     + - concatena listas
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#        0     1         2          3    4
#        -5    -4        -3         -2   -1
lista = [123, True, 'Luiz Otávio', 1.2, []] 
lista[-3] = 'Maria'
print(lista)
print(lista[2].upper(),lista[2].lower(), type(lista[2]))

#         0  1  2  3
lista = [10,20,30,40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50) 
lista.append(60)
lista.append(70)
ultimo_valor=lista.pop(3) 
print(lista, f'Removido {ultimo_valor}')
ultimo_valor=lista.pop()
print(lista, f'Removido {ultimo_valor}')
lista.append('Luiz')
nome = lista.pop()
print(lista, nome)
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(0,5)
print(lista)

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
print(lista_c)

lista_a.extend(lista_b)
print(lista_a)