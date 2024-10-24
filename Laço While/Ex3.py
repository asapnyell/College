#Construir um algoritmo que calcule a média
# aritmética de vários valores
#inteiros positivos, digitados pelo usuário.
# O final da leitura acontecerá
#quando for lido um valor negativo.

soma_numero = 0
n = int(input('Digite o valor: '))
if n >=0:
    soma_numero =n
    while n >= 0:
        n = int(input('Digite o valor: '))
        if n >= 0:
            soma_numero = soma_numero + n
print(soma_numero)