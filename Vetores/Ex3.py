# Implemente um funcao que retorne o maior elemento de um
# vetor de inteiro
def maior_elemento(vetores):
    maior = vetores[0]
    for i in range(len(vetores)):
        if vetores[i] > maior:
            maior = vetores[i]
    return maior
vetores = [-50,2,3,4,5,6,7,8,9,-9]
print(maior_elemento(vetores))