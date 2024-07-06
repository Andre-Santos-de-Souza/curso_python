import random
import os

while True:
    print("Escolha o tipo de dado:")
    print("1. Moeda (Cara ou Coroa)")
    print("2. Dado de 6 lados")
    print("3. Dado de 8 lados")
    print("4. Dado de 12 lados")
    print("5. Dado de 20 lados")

    opcao = int(input("Digite o número da sua escolha: "))

    if opcao == 1:
        os.system('cls')
        print(f"O resultado da moeda foi: ", random.choice(['Cara','Coroa']))
    elif opcao == 2:
        os.system('cls')
        inteiro = random.randint(1, 6)
        print(f"Resultado do dado de 6 lados: ", inteiro)
    elif opcao == 3:
        os.system('cls')
        inteiro = random.randint(1, 8)
        print(f"Resultado do dado de 8 lados: ",inteiro)
    elif opcao == 4:
        os.system('cls')
        inteiro = random.randint(1, 12)
        print(f"Resultado do dado de 12 lados: ", inteiro)
    elif opcao == 5:
        os.system('cls')
        inteiro = random.randint(1, 20)
        print(f"Resultado do dado de 20 lados: ", inteiro)
    elif opcao > 5:
        print("Finalizado")
        break