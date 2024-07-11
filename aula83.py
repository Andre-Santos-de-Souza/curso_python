# Empacotamento e desempacotamento de dicionário
a,b =1,2
a,b = b,a
print(a,b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}

a,b = pessoa.values()
print(a,b)
a,b = pessoa.items()
print(a,b)
a,b = pessoa
print(a,b)
(a1, a2),(b1,b2) = pessoa.items()
print()

for chave,valor in pessoa.items():
    print(chave,valor)
print()

pessoa2 = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.60
}

pessoas_completa = {*pessoa}
print(pessoas_completa)
pessoas_completa = {**pessoa}
print(pessoas_completa)
pessoas_completa = {**pessoa, 'nome':1}
print(pessoas_completa)
pessoas_completa = {**pessoa, **dados_pessoa}
print(pessoas_completa)
print()

def mostro_argumentos_nomeados1(*args, **kwargs):
    print(*args,*kwargs)
    print(*args,*kwargs.values())
    print(*args,*kwargs.items())
    print(*args,kwargs.items())
    print(args,kwargs)
    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados1(1,2,3,nome='Joana', idade=23)
print()

def mostro_argumentos_nomeados2(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)
mostro_argumentos_nomeados2(**pessoas_completa)
print()

configuracoes = {
    'arg1':1,
    'arg2':2,
    'arg3':3,
    'arg4':4
}
def mostro_argumentos_nomeados3(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)
mostro_argumentos_nomeados3(**configuracoes)