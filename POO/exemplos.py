def fibonacci_recursivo(n):
   # Casos base da recursão
   if n <= 1:
       return n
   else:
       # Chamada recursiva para somar os dois termos anteriores
       return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

# Exemplo de uso:
valor = 10
print(fibonacci_recursivo(valor)) # Saída: 55

# 7) Maior entre três números
print("Encontrar o maior número entre três números.")
primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))
terceiro_numero = int(input("Digite o terceiro número: "))

def maior_de_tres(numero_primeiro, numero_segundo, numero_terceiro):
    if numero_primeiro >= numero_segundo and numero_primeiro >= numero_terceiro:
        return numero_primeiro
    elif numero_segundo >= numero_primeiro and numero_segundo >= numero_terceiro:
        return numero_segundo
    else:
        return numero_terceiro

maior = maior_de_tres(primeiro_numero, segundo_numero, terceiro_numero)
print(f"O maior número é: {maior}")

# 20) Função Fibonacci
print("Função para gerar sequência de Fibonacci.")
valor = int(input("Digite um número para calcular o Fibonacci: "))
def fibonacci(n):
   if n == 1:
    return 1
   else:
      return n * fibonacci(n-1)

print(f"Fibonacci: ""{valor}""", fibonacci(valor))

