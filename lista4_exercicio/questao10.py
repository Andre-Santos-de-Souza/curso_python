def verificar_polindromo(palavra):
    palavra_invertida = palavra[::-1]
    if palavra_invertida == palavra:
        return "A palavra fornecida é um palíndromo."
    else:
        return "A palavra fornecida não é um palíndromo."

palavra = input("Digite uma palavra: ")
funcao = verificar_polindromo(palavra.lower())
print(funcao)