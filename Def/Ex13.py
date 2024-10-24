#Faça um algoritmo que leia uma
# quantidade não determinada de números
#positivos. Calcule a quantidade de números
# pares e ímpares, a média de
#valores pares e a média geral dos números lidos. O número que
#encerrará a leitura será zero.

def imparorpar():
    par = 0
    impar = 0
    while True:
        numero = int(input('Digite um numero: '))
        if numero <=-1:
            print('INVALIDO! SOMENTE INTEIRO POSITIVO')
            continue
        if numero == 0:
            break
        if numero % 2 == 0:
                par += 1
        else:
            impar += 1
    return par, impar
par,impar = imparorpar()
print(f'Par = {par}\nImpar = {impar}')