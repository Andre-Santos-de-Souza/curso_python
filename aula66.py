"""
Argumentos nomeados e não nomeados em funções Python
Argumentos nomeados tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x,y,z):
    # Definição
    print(f'{x=} y={y} z={z}', '|','x + y =',x+y+z)

soma(1,2,3)# argumentos não nomeados ou argumentos posicionais recebem apenas o valor para preencher o parâmetro na ordem
soma(1,y=2,z=5)# argumentos nomeados recebem o nome do parâmetro antes do valor

print(1,2,3,sep='-')