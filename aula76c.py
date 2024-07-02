# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda 3',
}
print(len(pessoa))
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
pessoa.setdefault('idade',30)
print(pessoa['idade'])

print()

for valor in pessoa.keys():
    print(valor)
print()

for valor in pessoa.values():
    print(valor)
print()

for chave, valor in pessoa.items():
    print(chave,valor)
print()