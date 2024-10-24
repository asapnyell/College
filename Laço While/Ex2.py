#Chico tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem
#1,30 metro e cresce 3 centímetros por ano. Construa um algoritmo que
#calcule e imprima quantos anos serão necessários para que Zé seja
#maior que Chico.

altura_chico = 1.50
altura_ze = 1.30
cresc_chico = 0.02
cresc_ze = 0.03

anos = 0

while altura_ze <= altura_chico:
    altura_chico = altura_chico + cresc_chico
    altura_ze += cresc_ze
    anos += 1

# Imprimindo o resultado
print('Zé será maior que Chico em', anos, 'anos.')