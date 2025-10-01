import math


class Usuario:

    def __init__(self,nome):
        self.nome = nome
    def getNome(self):
        return self.nome
    def setNome(self,nome): 
        self.nome = nome

pessoa = Usuario("")
print("Bem-vindo(a) ao programa de exercícios!\n")
# 1) Leia um nome do usuário e imprima: Olá, <nome>!

nome = input("Digite seu nome: ")
pessoa.setNome(nome)
print(f"Olá, {pessoa.getNome()}! Seja bem-vindo(a)!")

print("\n")
# 2) Leia dois números inteiros, converta e exiba a soma

print("Vamos somar dois números inteiros.")
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

def somar(a, b):
    return a + b

print(f"A soma entre {numero1} + {numero2} é: {somar(numero1, numero2)}")

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
numero = int(input("Digite um número inteiro: "))

def par_impar(numero):
    if numero % 2 == 0:
        return "Par"
    return "Ímpar"

print(f"O número {numero} é: {par_impar(numero)}")

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
    
print(f"Situação do aluno {nome}: {situacao(media)}") # Aqui peguei o nome que foi instanciado em de Pessoa()


print("\n")
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
    
maior = maior_de_tres(primeiro_numero,segundo_numero,terceiro_numero)
print(f"O maior número é: {maior}")

print("\n")
# 8) Verificar ano bissexto
print("Verificar se um ano é bissexto.")
ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto")
else:
    print(f"{ano} não é um ano bissexto")

print("\n")
# 9) Contagem regressiva
print("Contagem regressiva.")
valor = int(input("Digite um número para a contagem regressiva: "))
while valor >= 0:
    print(valor)
    valor -= 1

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
        continue
print(f"Parabéns! Você acertou! o numero secreto é {numero_secreto}.")

print("\n")
# 13) Tabuada
print("Tabuada de um número.")
valor = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{valor} x {i} = {valor * i}")

print("\n")
# 14) Contar vogais em uma string
print("Contar vogais em uma frase.")
texto = input("Digite uma frase: ").lower()
vogais = "aeiou"
contador = 0
for letra in texto:
    if letra in vogais:
        contador += 1
print(f"Número de vogais na frase '{texto}': {contador}")

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
def fibonacci(n):
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

print("Fibonacci (10 termos):", fibonacci(10))
print("Fibonacci (5 termos):", fibonacci(5))