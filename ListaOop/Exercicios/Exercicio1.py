class Funcionario:
    def __init__ (self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def exibir_dados(self):
        print ( f"Nome: {self.nome}, Cargo: {self.cargo}, Salário: R${self.salario}")
    
    def __str__(self):
        return f"{self.nome} - {self.cargo}"


funcionario1 = Funcionario("Maria", "Analista de Sistemas", 4500.00)

funcionario2 = Funcionario("João", "Desenvolvedor", 5000.00)

funcionario1.exibir_dados()
funcionario2.exibir_dados()


print(funcionario1)
print(funcionario2)