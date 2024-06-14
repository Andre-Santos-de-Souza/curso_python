# Problema "dentro_fora"

valor_x = int(input("Quantos numeros voce vai digitar? "))

dentro = 0
fora = 0
for i in range(0, valor_x):
    numero_int = int(input('Digite um numero: '))

    if numero_int >= 10 and numero_int <= 20:
        dentro += 1
    else:
        fora += 1

print(f'{dentro} DENTRO')
print(f'{fora} FORA')