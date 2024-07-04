def remover_elemento(set,numero):
    if numero in set:
        set.discard(numero)
        return set
    
set1, numero =  {1, 2, 3}, 2
funcao = remover_elemento(set1,numero)
print(funcao)