import os

notas = []
frequencias = []
while True:
    print("Adicione a nota final de cada aulno e o número de faltas")
    nota_final_aluno = float(input("Digite a nota final de 0 a 10: "))
    frequencia_aluno = int(input("Digite o número de faltas: "))

    if nota_final_aluno < 5:
        os.system('cls')
        print("Seu conceito é INSUFICIENTE")
    elif nota_final_aluno <= 5 and nota_final_aluno < 7:
        os.system('cls')
        print("Seu conceito é REGULAR")
    elif nota_final_aluno <= 7 and nota_final_aluno < 9:
        os.system('cls')
        print("Seu conceito é BOM")
    elif nota_final_aluno <= 10:
        os.system('cls')
        print("Seu conceito é EXCELENTE")
    else:
        print("Digite apenas as notas de 0 a 10.")
        print()

    if frequencia_aluno < 75:
        print('Aluno reprovado por falta')
    else:
        print('Aluno não reprovado por falta')

    notas.append(nota_final_aluno)
    frequencias.append(frequencia_aluno)

    continuar = input("Deseja adicionar mais alunos? (s/n): ").strip().lower()
    if continuar != 's':
        break

while True:
    print("\nMenu Interativo:")
    print("1. Imprimir o total de alunos lidos.")
    print("2. Imprimir a maior nota da turma.")
    print("3. Imprimir a menor nota da turma.")
    print("4. Imprimir a média das notas da turma.")
    print("5. Imprimir a porcentagem de alunos reprovados por falta.")
    print("6. Sair.")
    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        alunos_lidos = len(notas)
        print(f"O número total de alunos lidos {alunos_lidos}")
    elif opcao == 2:
        maior_nota = max(notas)
        print(f"A maior nota é {maior_nota}")
    elif opcao == 3:
        menor_nota = min(notas)
        print(f"A menor nota é {menor_nota}")
    elif opcao == 4:
        media = sum(notas)/len(notas)
        print(f"A média das notas da turma é {media} ")
    elif opcao == 5:
        reprovados_por_falta = sum(1 for frequencia in frequencias if frequencia < 75)
        porcentagem_reprovados = (reprovados_por_falta / len(frequencias)) * 100 if frequencias else 0
        print(f"A porcentagem de alunos reprovados por falta é: {porcentagem_reprovados:.2f}%")
    else:
        print("Finalizado")
        break