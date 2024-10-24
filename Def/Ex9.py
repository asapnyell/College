# escreva um algortimo que leia 20 valores
#e encontre o maior e menor deles
# mostre o resultado
def numero_maior():
    n = int(input("Digite o valor: "))
    maior = n
    menor = n
    for i in range(9):
        n = int(input("Digite o valor: "))
        if n > maior:
            maior = n
        if n < menor:
                menor = n
    return maior, menor

maior, menor  = numero_maior()
print(maior)
print(menor)