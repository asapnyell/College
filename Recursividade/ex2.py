#Escreva um algoritmo recursivo para avaliar a * b usando a adição, onde a e b são inteiros não negativos e não nulos.

def produto (a,b):
    if b == 1:
        return a
    if b > 1:
        return produto(a,b -1) + a
    
print(produto(5,50))
