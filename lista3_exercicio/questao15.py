# Problema "fatorial"

n = int(input("Digite um número natural (máximo 15): "))
while n < 0 or n > 15:
    print("Por favor, insira um número entre 0 e 15.")
    n = int(input("Digite um número natural (máximo 15): "))

fatorial = 1
for i in range(1, n + 1):
    fatorial *= i

print(f"O fatorial de {n} é {fatorial}")