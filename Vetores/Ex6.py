#Escrever uma função que recebe por parâmetro um vetor de inteiros e
#retorna a soma de seus elementos.      

def soma(vetores):
    aux = 0
    for i in range(len(vetores)):
        aux += vetores[i]
    return aux
vetores = [1,2,3,4,5,6,7,8,9,10]
vetor_somado = soma(vetores)
print(vetor_somado)