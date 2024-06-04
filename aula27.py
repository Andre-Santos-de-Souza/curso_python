"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
obs.: a função "len" retorna a qtd de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[4])
print(variavel[4:])
print(variavel[4:7])
print(variavel[:5])
print(variavel[0:5])
print(variavel[-8:-2])
print(len(variavel))

# 0: É o índice inicial, indicando onde o fatiamento começa. O índice 0 representa o primeiro elemento da string ou lista.
# 9: É o índice final, indicando onde o fatiamento termina (não inclusivo). O elemento com o índice 9 não será incluído no resultado.
# 2: É o passo (step), que indica quantos elementos devem ser pulados entre cada item selecionado.
print(variavel[0:9:2])
print(variavel[-1:-10:-1])
print(variavel[::-1])