#Escrever uma função contarImpar(n1, n2) que retorna
#o número de inteiros ímpares que existem entre n1 e
#n2 (inclusive ambos, se for o caso). A função deve
#funcionar inclusive se o valor de n2 for menor que n1.

def contar_impar(n1, n2):
    quantidade = 0
    for i in range (n1 +n2):
        if i % 2 == 1:
            quantidade += 1
    return quantidade
n1 = int(input("Digite o o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
resultado = contar_impar(n1, n2)
print(resultado)