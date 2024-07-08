contador_de_alunos = 0

for numero_de_vezes in range(1,10+1):
    contador_de_alunos+=1
    print(f"Digite as notas do {contador_de_alunos}° aluno:")

    nota_1 = float(input("Digite a primeira nota: "))
    nota_2 = float(input("Digite a segunda nota: "))

    media_ponderada = (nota_1*4 + nota_2*6)/(4+6)

    if media_ponderada < 4.9:
        print('INSUFICIENTE')
        print()
    elif media_ponderada >= 5.0 and media_ponderada <= 6.9:
        print("REGULAR")
        print()
    elif media_ponderada >= 7.0 and media_ponderada <= 8.9:
        print("BOM")
        print()
    elif media_ponderada >= 9.0 and media_ponderada <= 10.0:
        print("EXCELENTE")
        print()