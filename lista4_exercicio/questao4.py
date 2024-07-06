import math
import os
while True:
    print('1. Adição')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('5. Exponenciação')
    print('6. Raiz quadrada')
    print('7. Equação de segundo grau')
    print('8. Sair')
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        os.system('cls')
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite outro número: "))
        adicao = n1+n2
        print(f"A adição = {adicao}")
    elif opcao == 2:
        os.system('cls')
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite outro número: "))
        subtracao = n1-n2
        print(f"A subtração = {subtracao}")
    elif opcao == 3:
        os.system('cls')
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite outro número: "))
        multiplicacao = n1*n2
        print(f"A multiplicação = {multiplicacao}")
    elif opcao == 4:
        os.system('cls')
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite outro número: "))
        divisao = n1/n2
        print(f"A divisão = {divisao}")
    elif opcao == 5:
        os.system('cls')
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite outro número: "))
        exponenciacao = n1 ** n2
        print(f"A dexponenciação = {exponenciacao}")
    elif opcao == 6:
        os.system('cls')
        n1 = float(input("Digite um número: "))
        raiz_quadrada = math.sqrt(n1)
        print(f"A raiz quadrada = {raiz_quadrada}")
    elif opcao == 7:
        os.system('cls')
        coeficiente_a = float(input("Digite o coeficiente a: "))
        coeficiente_b = float(input("Digite o coeficiente b: "))
        coeficiente_c = float(input("Digite o coeficiente c: "))
        delta = (coeficiente_b*coeficiente_b) - 4*coeficiente_a*coeficiente_c
        
        x1 = (- coeficiente_b + math.sqrt(delta)) / (2.0 * coeficiente_a)
        x2 = (- coeficiente_b - math.sqrt(delta)) / (2.0 * coeficiente_a)
        
        print("X1: ", x1)
        print("X2: ", x2)
        if(delta < 0):
            print("Esta equacao nao possui raizes reais");
    else:
        print("Finalizado")
        break