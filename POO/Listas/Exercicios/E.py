import math

# 17) Função média de 3 números
print("Função para calcular a média de três números.")
def media(a, b, c):
    return (a + b + c) / 3

print("Média:", media(7, 8, 9))

print("\n")
# 18) Função para verificar número primo
print("Função para verificar se um número é primo.")
def eh_primo(n):
    if n < 2: # Números menores ou iguais a 1, por definição, não são primos.
        return False
    for i in range(2, int(math.sqrt(n)) + 1): 
        if n % i == 0:
            return False
    return True

print("97 é primo?", eh_primo(97))
print("10 é primo?", eh_primo(10))

print("\n")
# 19) Função com parâmetro opcional
print("Função com parâmetro opcional.")
def saudar(nome, curso="Python"):
    return f"Olá, {nome}! Bem-vindo(a) ao curso de {curso}."

print(saudar("Maria"))
print(saudar("João", "Java"))

print("\n")
# 20) Função Fibonacci
print("Função para gerar sequência de Fibonacci.")
def fibonacci_recursivo(n):
   # Casos base da recursão
   if n <= 1:
       return n
   else:
       # Chamada recursiva para somar os dois termos anteriores
       return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

valor = int(input("Digite um número para calcular o Fibonacci: "))
print(fibonacci_recursivo(valor))