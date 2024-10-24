#Crie um programa que solicita ao usuário
#a entrada de 5 notas e calcula a média dessas notas.

soma= 0
for i in range(5):
    n = int(input('Digite o valor: '))
    soma += n
media = soma /5
print('Media=',media)