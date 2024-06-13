# Problema "tabuada"
try:
    numero_int = int(input('Deseja a tabuada para qual valor? '))
    for i in range(1,11):
        print(f'{numero_int} x {i} = {numero_int*i}')
except:
    print("Digite apenas números inteiros.")