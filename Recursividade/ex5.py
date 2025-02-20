#Soma com Recursão. A soma de dois números inteiros positivos não nulos, pode ser definida
#recursivamente utilizando a idéia do sucessor e antecessor de um número.
#A função soma de dois números inteiros positivos não nulos pode ser escrita da seguinte forma

def soma (a,b):
    if b == 0:
        return a
    elif b > a:
        return soma(b,a)
    return soma(a + 1,b - 1)

print(soma(5,3))