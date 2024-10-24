#faca um algoritmo que leia 10
# valores e imprima a quantidade de numeros
## negativos

quantidade = 0
for i in range (10):
    n = int(input('digite o valor: '))
    if n < 0:
       quantidade = quantidade + 1
print(quantidade)
