# Faca um algortimo que le um valor N inteiro
#e positivo e que calcule e escreva o
#fatorial de N(N!)
n = int(input('Digite um numero: '))
resultado = 1
for i in range (1,n+1):
    resultado = resultado * i
print('Fatorial de',n,'é',resultado)