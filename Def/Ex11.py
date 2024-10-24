#Faça um algoritmo que leia uma quantidade não determinada de números
#positivos. Calcule a quantidade de números pares e ímpares, a média de
#valores pares e a média geral dos números lidos. O número que
#encerrará a leitura será zero.

def par_ou_impar():
    quantidade_pares = 0
    quantidade_impares = 0
    numero = int(input("Digite o numero: "))
    while numero > 0:
        if numero % 2 == 0:
            quantidade_pares += 1
        else:
            quantidade_impares += 1
        numero = int(input("Digite o numero: "))
    return f"Impar {quantidade_impares}\n Par {quantidade_pares}"

qtd_par_impar = par_ou_impar()
print(qtd_par_impar)