import random
numero_aleatorio = random.randint(1, 100)
palpite=0
while numero_aleatorio != palpite:
    palpite = int(input("Adivinhe o número: "))
    if palpite > numero_aleatorio:
        print("O número fornecido é menor")
    else:
        print("O número fornecido é maior")

    if palpite == numero_aleatorio:
        print("Você acertou")
        break
    