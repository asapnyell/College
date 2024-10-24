#faca um algoritmo que leia 10
# valores e imprima a quantidade de numeros
## negativos

def numeros_negativos():
    quantidade = 0
    for i in range(10):
        n = int(input("Digite o valor: "))
        if n < 0:
            quantidade += 1
    return quantidade
soma_negativos = numeros_negativos()
print(soma_negativos)