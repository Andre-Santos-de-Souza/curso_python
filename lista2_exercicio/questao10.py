# Problema "multiplos"

try:
    print('Digite dois numeros inteiros: ')
    numero_1 = input('Digite o primeiro número: ')
    numero_2 = input('Digite o segundo número: ')

    numero_1 = int(numero_1)
    numero_2 = int(numero_2)

    if numero_1 % numero_2 == 0:
        print('São múltiplos')
    elif numero_2 % numero_1 == 0:
        print('São mútiplos')
    else:
        print('Não são múltiplos')
except:
    print('Digite apenas números inteiros.')