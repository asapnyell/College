class Usuario: #Aqui criei uma classe Usuario para armazenar o nome do usuário

    def __init__(self,nome):
        self.nome = nome
    def getNome(self):
        return self.nome
    def setNome(self,nome): 
        self.nome = nome

pessoa = Usuario("") #Aqui criei um objeto pessoa da classe Usuario com nome vazio
print("Bem-vindo(a) ao programa de exercícios!\n")
# 1) Leia um nome do usuário e imprima: Olá, <nome>!

nome = input("Digite seu nome: ") #Aqui peço para o usuário digitar o nome
pessoa.setNome(nome) #Aqui uso o método setNome para mudar o nome do objeto pessoa("") para o nome digitado pelo usuário
print(f"Olá, {pessoa.getNome()}! Seja bem-vindo(a)!")

print("\n")
# 2) Leia dois números inteiros, converta e exiba a soma

print("Vamos somar dois números inteiros.")
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

def somar(a, b): #Função que retorna a soma de dois números
    return a + b

print(f"A soma entre {numero1} + {numero2} é: {somar(numero1, numero2)}") #Aqui chamo a função somar e mostro o resultado

print("\n")
# 3) Leia três notas, calcule a média e mostre com 2 casas decimais

print("Vamos calcular a média de três notas.")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

def media(a, b, c): #Função que retorna a média de três números
    return (a + b + c) / 3

print(f"Média entre {nota1}, {nota2} e {nota3} é: {media(nota1, nota2, nota3):.2f}") #Aqui chamo a função media e mostro o resultado com 2 casas decimais

print("\n")
# 4) Leia o raio de um círculo e calcule a área (π * r²)

print("Vamos calcular a área de um círculo.")
raio = float(input("Digite o raio do círculo: "))
pi = 3.14159

def calcular_area(raio):
    return pi * (raio ** 2)

print(f"A área do círculo é: {calcular_area(raio):.2f}")
