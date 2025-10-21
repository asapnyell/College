"""
Crie uma hierarquia de classes simples:

Classe Funcionario com atributos nome e salario, e método exibir_informacoes().
Classe Professor (herda de Funcionario), que adiciona o atributo disciplina.
Classe Coordenador (herda de Funcionario), que adiciona o atributo setor.
Cada classe deve ter seu próprio método detalhes(), que exibe uma frase diferente, por exemplo:

Para Funcionario: “Funcionário <nome> recebe R$<salario>.”
Para Professor: “Professor <nome> ministra <disciplina> e recebe R$<salario>.”
Para Coordenador: “Coordenador <nome> é responsável pelo setor <setor>.”
Crie um objeto de cada classe e chame os métodos.
"""

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir_informacoes(self):
        return f"Funcionário {self.nome} recebe R${self.salario:.2f}."

class Professor(Funcionario):
    def __init__(self, nome, salario, disciplina):
        super().__init__(nome, salario) # Chama o construtor da classe base (Funcionario)
        self.disciplina = disciplina

    def exibir_informacoes(self):
        return f"Professor {self.nome} ministra {self.disciplina} e recebe R${self.salario:.2f}."

class Coordenador(Funcionario):
    def __init__(self, nome, salario, setor):
        super().__init__(nome, salario)
        self.setor = setor

    def exibir_informacoes(self):
        return f"Coordenador {self.nome} é responsável pelo setor {self.setor}."
    
# Testando as classes
funcionario = Funcionario("Carlos", 2000)
professor = Professor("Ana", 3500, "Matemática")
coordenador = Coordenador("Marcos", 4000, "TI")


print(funcionario.exibir_informacoes())
print(professor.exibir_informacoes())
print(coordenador.exibir_informacoes())