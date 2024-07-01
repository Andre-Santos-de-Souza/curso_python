def impares_pares(numeros):
    while True:
        contador1 = 0
        contador2 = 0
        for item in numeros:
            if item % 2 == 0:
                contador1 +=1
            else:
                contador2 +=1
        return contador1,contador2

lista = [1,2,3,4,5,6]
par,impar = impares_pares(lista)
print(f'Números pares: {par}, Números ímpares: {impar}')