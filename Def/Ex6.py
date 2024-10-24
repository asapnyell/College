#Escrever uma função somarIntervalo(n1, n2) que
#retorna a soma dos números inteiros que existem
#entre n1 e n2 (inclusive ambos). A função deve
#funcionar inclusive se o valor de n2 for menor que n1.

def somar_intervalo(n1, n2):
    soma = 0
    for i in range(n1, n2+1):
        soma += i
    return soma

n1 = int(input("Digite o valor 1: "))
n2 = int(input("Digite o valor 2: "))
soma = somar_intervalo(n1, n2)
print("A SOMA DO INTERVALO É",soma)