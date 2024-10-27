#Implemente uma função que retorne o menor elemento de um vetor de
#inteiros.

def menorElemento(valores):
    menor = valores[0]
    for i in range(len(valores)):
        if valores[i] < menor:
            menor = valores[i]
    return menor
valores = [10,9,8,7,6,5,4,1,3,50]
print(menorElemento(valores))
