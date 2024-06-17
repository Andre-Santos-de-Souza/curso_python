"""
Você recebeu uma lista de números inteiros e precisa realizar as seguintes operações usando funções em Python:

1-Encontre e retorne o maior número da lista.
2-Encontre e retorne o menor número da lista.
3-Calcule e retorne a média dos números da lista.
4-Remova todos os números pares da lista e retorne a lista resultante.
"""

numeros = [10, 5, 8, 3, 12, 7, 1, 4, 9]

maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)
media = soma / len(numeros)

lista_sem_pares = [i for i in numeros if i % 2 != 0]

print("Maior número:", maior)
print("Menor número:", menor)
print("Média dos números:", media)
print("Lista sem números pares:", lista_sem_pares)