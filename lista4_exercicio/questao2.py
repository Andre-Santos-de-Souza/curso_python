a = float(input("Digite o comprimento do lado a: "))
b = float(input("Digite o comprimento do lado b: "))
c = float(input("Digite o comprimento do lado c: "))

if a == b and a == c:
    print('Equilátero')
elif a <= 0 or b <= 0 or c <= 0:
    print("Inválido")
elif a == b and a != c or a == c and a != b:
    print("Isósceles")
elif a != b and a != c:
    print("Escaleno")
