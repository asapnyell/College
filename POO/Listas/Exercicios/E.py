
# 17) Função média de 3 números
print("Função para calcular a média de três números.")
def media(a, b, c):
    return (a + b + c) / 3

print("Média:", media(7, 8, 9))

print("\n")
# 18) Função para verificar número primo 
print("Função para verificar se um número é primo.")

def eh_primo(n):
    if n < 2:  # Números menores que 2 não são primos
        return False

    #  elevar (n)**0.5 é o mesmo que raiz quadrada. 
    raiz = int(n ** 0.5) + 1 # +1 para incluir a raiz na verificação. Para descobrir se "n" tem algum divisor além de 1 e ele mesmo, basta procurar por divisores até a sua raiz quadrada. 
    for i in range(2, raiz):
        if n % i == 0:  # Se n for divisível por i, não é primo
            return False
    return True  # Se não encontrou divisores, é primo

# Testando a função
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