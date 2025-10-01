class User:

    def __init__(self,nome):
        self.nome = nome
    def getNome(self):
        return self.nome
    def setNome(self,nome): 
        self.nome = nome

pessoa = User("")
print("Bem-vindo(a) ao programa de exercícios!\n")
# 1) Leia um nome do usuário e imprima: Olá, <nome>!

nome = input("Digite seu nome: ")
pessoa.setNome(nome)
print(f"Olá, {pessoa.getNome()}! Seja bem-vindo(a)!")
