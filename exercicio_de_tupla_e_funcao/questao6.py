def intercalar_tuplas(tupla1,tupla2):
    tupla_3 = [elem for pair in zip(tupla1, tupla2) for elem in pair]
    return tuple(tupla_3)

tupla_1 = (1,2,3)
tupla_2 = ('a','b','c')
funcao = intercalar_tuplas(tupla_1,tupla_2)
print(funcao)