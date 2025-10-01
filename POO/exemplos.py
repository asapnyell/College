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
def fibonacci(n):
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

print("Fibonacci (10 termos):", fibonacci(10))
print("Fibonacci (5 termos):", fibonacci(5))