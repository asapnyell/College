#Maior e menor elemento de um vetor e soma dos seus
#elementos. Imagine a como um vetor de
#inteiros. Apresente algoritmos recursivos para calcular:
#a) O elemento máximo do vetor
#b) O elemento mínimo do vetor
#c) A soma dos elementos do veto

import random

def vetor():
    a = random.sample(range (1,100),10)
    return a

def max_element(lista):
    max = lista[0]
    for i in lista:
        if i > max:
            max = i
    return max

def min_element(lista):
    min = lista[0]
    for i in lista:
        if i < min:
            min = i
    return min

def soma(lista):
    total = 0
    for i in lista:
        total += i
    return total

lista = vetor()
print(f'Vetor: {lista}')
print(f'Maior elemento: {max_element(lista)}')
print(f'Menor elemento: {min_element(lista)}')
print(f'A soma dos elementos é: {soma(lista)}')