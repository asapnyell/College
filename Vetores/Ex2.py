#Escrever uma funcao que receba um vetor com 10 valores e
#retorne quantos destes valores sao negativos
def contarNegativo(valores):
    negativos = 0
    for i in range(len(valores)):
        if valores[i] < 0:
            negativos +=1
    return negativos
valores = [1,-2,3,-4,5,-6,7,-8,9,-10]
print(contarNegativo(valores))
