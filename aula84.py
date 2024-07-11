# List comprehension em python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
import pprint

def p(v):
    pprint.pprint(novos_produtos, sort_dicts=False, width=40)

lista = []

for numero in range(10):
    lista.append(numero)
print(lista)
print()

lista = [
    numero *2
    for numero in range(10)
    ]
print(list(range(10)))
print(lista)
print()

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} if produto['preco'] > 20 else {**produto} for produto in produtos
]

# print(novos_produtos)
# print(*novos_produtos, sep='\n')
# p(novos_produtos)
# lista = [n for n in range(10) if n < 5]
novos_produtos = [
    # O que vem na esquerda do for é 'mapeamento'.
    # O que vem na direita do for é 'filtro'
    {**produto, 'preco': produto['preco'] * 1.05} if produto['preco'] > 20 else {**produto} for produto in produtos if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
]
p(novos_produtos)