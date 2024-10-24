# escreva um algortimo que leia 20 valores
#e encontre o maior e menor deles
# mostre o resultado
q_maior = 0
q_menor = 0
for i in range (10):
    n = int(input('digite o valor: '))
    if n > q_maior:
        q_maior = n
    if n < q_menor:
        q_menor = n
print('o maior numero é :', q_maior)
print('o menor numero é: ', q_menor)