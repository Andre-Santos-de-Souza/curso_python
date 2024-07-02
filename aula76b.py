# Manipulando chaves e valores em dicionários
pessoa = {
    
}

chave = 'nome'
pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'
print(pessoa[chave])
# del pessoa['sobrenome']
if pessoa.get('sobrenome') is not None:
    print(pessoa['sobrenome'])
else:
    print("Não existe")

pessoa[chave] = 'Maria'
print(pessoa)
print(pessoa['nome'])