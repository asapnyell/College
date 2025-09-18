# 1) Leia um nome do usuário e imprima: Olá, <nome>!

nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")

# 2) Leia dois números inteiros, converta e exiba a soma

print("Vamos somar dois números inteiros.")
n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))

def somar(a, b):
    return a + b

print(f"A soma é: {somar(n1, n2)}")

# 3) Leia três notas (float), calcule a média e mostre com 2 casas decimais

print("Vamos calcular a média de três notas.")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

def media(a, b, c):
    return (a + b + c) / 3

print(f"Média = {media(nota1, nota2, nota3):.2f}")

# 4) Leia o raio de um círculo e calcule a área (π * r²)

print("Vamos calcular a área de um círculo.")
raio = float(input("Digite o raio do círculo: "))
pi = 3.14159

def calcular_area(raio):
    return pi * (raio ** 2)

print(f"A área do círculo é: {calcular_area(raio):.2f}")

# 5) Informe se o número é par ou ímpar
num = int(input("Digite um número inteiro: "))
if num % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")

# 6) Situação do aluno pela média
media = float(input("Digite a média do aluno: "))
if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")

# 7) Maior entre três números
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
print(f"O maior número é: {maior}")

# 8) Verificar ano bissexto
ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Ano bissexto")
else:
    print("Ano não bissexto")

# 9) Contagem regressiva
n = int(input("Digite um número para a contagem regressiva: "))
while n >= 0:
    print(n)
    n -= 1

# 10) Sistema de senha
senha_correta = "python123"
tentativas = 0
senha = ""
while senha != senha_correta and tentativas < 3:
    senha = input("Digite a senha: ")
    tentativas += 1
if senha == senha_correta:
    print("Acesso permitido!")
else:
    print("Acesso negado! Número de tentativas excedido.")

# 11) Soma de números até 'sair'
soma = 0
while True:
    entrada = input("Digite um número ou 'sair' para encerrar: ")
    if entrada.lower() == "sair":
        break
    soma += float(entrada)
print(f"A soma dos números digitados é: {soma}")

# 12) Jogo de adivinhação
numero_secreto = 37
palpite = -1
while palpite != numero_secreto:
    palpite = int(input("Digite seu palpite: "))
    if palpite < numero_secreto:
        print("O número secreto é maior!")
    elif palpite > numero_secreto:
        print("O número secreto é menor!")
print("Parabéns! Você acertou!")

# 13) Tabuada
n = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# 14) Contar vogais em uma string
texto = input("Digite uma frase: ").lower()
vogais = "aeiou"
contador = 0
for letra in texto:
    if letra in vogais:
        contador += 1
print(f"Número de vogais: {contador}")

# 15) Múltiplos de 3 de 1 a 100
print("Múltiplos de 3 entre 1 e 100:")
for i in range(1, 101):
    if i % 3 == 0:
        print(i, end=" ")
print()

# 16) Fatorial com for
n = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1
for i in range(1, n + 1):
    fatorial *= i
print(f"{n}! = {fatorial}")

# 17) Função média de 3 números
def media3(a, b, c):
    return (a + b + c) / 3

print("Média:", media3(7, 8, 9))

# 18) Função para verificar número primo
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("7 é primo?", eh_primo(7))
print("10 é primo?", eh_primo(10))

# 19) Função com parâmetro opcional
def saudar(nome, curso="Python"):
    return f"Olá, {nome}! Bem-vindo(a) ao curso de {curso}."

print(saudar("Maria"))
print(saudar("João", "Java"))

# 20) Função Fibonacci
def fibonacci(n):
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

print("Fibonacci (10 termos):", fibonacci(10))
print("Fibonacci (5 termos):", fibonacci(5))