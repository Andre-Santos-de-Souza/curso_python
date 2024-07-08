lista_1 = [0,1,0,3,12]
lista_2 = []
for i in lista_1:
    if i != 0:
        lista_2.append(i)

for i in lista_1:
    if i == 0:
        lista_2.append(i)

print(lista_2)
