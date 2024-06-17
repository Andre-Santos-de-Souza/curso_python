'''
Lista de listas e seus índices
'''
salas =[
    # 0        1
    ['Maria', 'Helena',], # 0
    # 0
    ['Elaine', ], # 1
    # 0     # 1      # 2
    ['Luiz', 'João','Eduardo', ] # 2
]
# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][3])

for salas in salas:
    print(f'A sala é {salas}')
    for aluno in salas:
        print(aluno)