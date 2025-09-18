class Pessoa:

    def __init__(self):
        self.nome = ''
    def getNome(self):
        return self.nome
    def setNome(self,nome): 
        self.nome = nome

pessoa = Pessoa()

# 1) Leia um nome do usuário e imprima: Olá, <nome>!

nome = input("Digite seu nome: ")
pessoa.setNome(nome)
print(f"Olá, {pessoa.getNome()}!")

print("\n")
# 2) Leia dois números inteiros, converta e exiba a soma

print("Vamos somar dois números inteiros.")
n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))

def somar(a, b):
    return a + b

print(f"A soma entre {n1} + {n2} é: {somar(n1, n2)}")

print("\n")
# 3) Leia três notas, calcule a média e mostre com 2 casas decimais

print("Vamos calcular a média de três notas.")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

def media(a, b, c):
    return (a + b + c) / 3

print(f"Média entre {nota1}, {nota2} e {nota3} é: {media(nota1, nota2, nota3):.2f}")

print("\n")
# 4) Leia o raio de um círculo e calcule a área (π * r²)

print("Vamos calcular a área de um círculo.")
raio = float(input("Digite o raio do círculo: "))
pi = 3.14159

def calcular_area(raio):
    return pi * (raio ** 2)

print(f"A área do círculo é: {calcular_area(raio):.2f}")

print("\n")
# 5) Informe se o número é par ou ímpar
print("Verificar se um número é par ou ímpar.")
num = int(input("Digite um número inteiro: "))

def eh_par(n):
    if n % 2 == 0:
        return True
    return False

if eh_par(num):
    print(f"O número {num} é par")
else:
    print(f"O número {num} é ímpar")

print("\n")
# 6) Situação do aluno pela média
print("Verificar a situação do aluno pela média.")
media = float(input("Digite a média do aluno: "))


def situacao(media):

    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"
    
print(f"Situação do aluno {nome}: {situacao(media)}")

print("\n")
# 7) Maior entre três números
print("Encontrar o maior número entre três números.")
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
print(f"O maior número é: {maior}")

print("\n")
# 8) Verificar ano bissexto
print("Verificar se um ano é bissexto.")
ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Ano bissexto")
else:
    print("Ano não bissexto")
""""""
print("\n")
# 9) Contagem regressiva
print("Contagem regressiva.")
n = int(input("Digite um número para a contagem regressiva: "))
while n >= 0:
    print(n)
    n -= 1

print("\n")
# 10) Sistema de senha
print("Sistema de senha. Você tem 3 tentativas.")
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

print("\n")
# 11) Soma de números até 'sair'
print("Soma de números. Digite 'sair' para encerrar.")
soma = 0
while True:
    entrada = input("Digite um número ou 'sair' para encerrar: ")
    if entrada.lower() == "sair":
        break
    soma += float(entrada)
print(f"A soma dos números digitados é: {soma}")

print("\n")
# 12) Jogo de adivinhação
print("Jogo de adivinhação. Tente adivinhar o número secreto entre 1 e 10.")
numero_secreto = 5
palpite = -1
while palpite != numero_secreto:
    palpite = int(input("Digite seu palpite: "))
    if palpite < numero_secreto:
        print("O número secreto é maior!")
    elif palpite > numero_secreto:
        print("O número secreto é menor!")
print("Parabéns! Você acertou!")

print("\n")
# 13) Tabuada
print("Tabuada de um número.")
n = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

print("\n")
# 14) Contar vogais em uma string
print("Contar vogais em uma frase.")
texto = input("Digite uma frase: ").lower()
vogais = "aeiou"
contador = 0
for letra in texto:
    if letra in vogais:
        contador += 1
print(f"Número de vogais: {contador}")

print("\n")
# 15) Múltiplos de 3 de 1 a 100
print("Encontrar múltiplos de 3 entre 1 e 100.")
print("Múltiplos de 3 entre 1 e 100:")
for i in range(1, 101):
    if i % 3 == 0:
        print(i, end=", ")
print()

print("\n")
# 16) Fatorial com for
print("Calcular o fatorial de um número.")
n = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1
for i in range(1, n + 1):
    fatorial *= i
print(f"{n}! = {fatorial}")

print("\n")
# 17) Função média de 3 números
print("Função para calcular a média de três números.")
def media3(a, b, c):
    return (a + b + c) / 3

print("Média:", media3(7, 8, 9))

print("\n")
# 18) Função para verificar número primo
print("Função para verificar se um número é primo.")
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("7 é primo?", eh_primo(7))
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
def fibonacci(n):
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

print("Fibonacci (10 termos):", fibonacci(10))
print("Fibonacci (5 termos):", fibonacci(5))