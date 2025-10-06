# 13) Tabuada
print("Tabuada de um número.")
valor = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11): # Loop de 1 a 10
    print(f"{valor} x {i} = {valor * i}") # A cada interação o Índece "i" que vai de 1 a 10 é multiplicado pelo "valor".

print("\n")
# 14) Contar vogais em uma string
print("Contar vogais em uma frase.")
texto = input("Digite uma frase: ").lower()
vogais = "aeiou"
contador = 0
for letra in texto: #Loop para cada letra no texto informado, Texto é um "array" de string
    if letra in vogais: # Verificada cada letra do texto, e verifica se consta em "vogais"
        contador += 1 #Se sim, adiciona +1 ao contador, que se inicia em 0.
print(f"Número de vogais na frase '{texto}': {contador}")

print("\n")
# 15) Múltiplos de 3 de 1 a 100
print("Encontrar múltiplos de 3 entre 1 e 100.")
print("Múltiplos de 3 entre 1 e 100:")
for i in range(1, 101): # Range de 1 a 100
    if i % 3 == 0: # Pega cada indice de 1 a 100 e verifica se o resto da divisao é 0.
        print(i, end=", ") # Se sim, printa o ìndice. 
print("\b\b.")

print("\n")
# 16) Fatorial com for
print("Calcular o fatorial de um número.")
valor = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1
for i in range(1, valor + 1):
    fatorial *= i
print(f"{valor}! = {fatorial}")