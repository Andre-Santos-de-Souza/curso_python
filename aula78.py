# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
s1 = set() # set vazio
s1 = {'Luiz',1,2,3} # set com dados 

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

li = [1,2,3,3,3,3,3,1]
s1 = set(li)
l2 = list(s1)
print(l2)
s1 = {1,2,3}
print(s1)
# print(3 not in s1)
# print(3 in s1)
# for numero in s1:
#     print(numero)
print()

# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add('Luiz')
s1.add(1)
print(s1)
s1.update("Olá, Mundo")
s1.update(("Olá, Mundo",1,2,3,4))
print(s1)
# s1.clear()
s1.discard("Olá, Mundo")
s1.discard("Luiz")
print(s1)
print()

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 | s2 #união
print(s3)
s3 = s1 & s2 #intersecção
print(s3)
s3 = s2 - s1 #diferença
print(s3)
s3 = s2 ^ s1 #diferença simétrica
print(s3)