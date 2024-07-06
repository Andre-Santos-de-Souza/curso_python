N = int(input("Digite um número inteiro: "))

notas = [100, 50, 20, 10, 5, 2, 1]

resultado = []

valor_restante = N

for nota in notas:
    quantidade = valor_restante // nota
    resultado.append(quantidade)
    valor_restante = valor_restante % nota

print(f"{N}")
for i in range(len(notas)):
    print(f"{resultado[i]} nota(s) de R$ {notas[i]},00")