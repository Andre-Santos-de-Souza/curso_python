# Problema "par_impar"

valor_x = int(input("Quantos numeros voce vai digitar? "))

for i in range(0, valor_x):
    numero_int = int(input('Digite um numero: '))

    if numero_int < 0:
        if numero_int % 2 == 0:
            print("PAR NEGATIVO") 
        else:
            print("ÍMPAR NEGATIVO")
    elif numero_int > 0:
        if numero_int % 2 == 0:
            print("PAR  POSITIVO")
        else:
            print("ÍMPAR POSITIVO")
    else:
        print("NULO")
            