"""
Crie a classe Funcionario com atributos nome e salario.
Crie a subclasse Gerente, que possui também setor.
Sobrescreva o método __str__ para mostrar todas as informações.

"""
class Funcionario: # Classe base Funcionario
 
    def __init__(self, nome: str, salario: float): # Construtor da classe Funcionario. tipando os parâmetros.

        self._nome = nome #atributo protegido
        self._salario = salario #atributo protegido

    # Sobrescrevendo o método mágico __str__
    def __str__(self):
        """
        Retorna uma representação em string do objeto Funcionario.
        """
        return f" Nome: {self._nome}, Salário: R$ {self._salario:.2f}"


# Definindo a subclasse Gerente, que herda de Funcionario
class Gerente(Funcionario):
    """
    Subclasse que representa um Gerente, herdando de Funcionario.
    Possui o atributo específico 'setor'.
    """
    def __init__(self, nome: str, salario: float, setor: str):
        """
        Construtor da classe Gerente.
        """
        # Chamando o construtor da classe base (Funcionario)
        super().__init__(nome, salario)
        self._setor = setor # Atributo específico de Gerente

    # Sobrescrevendo o método mágico __str__ para incluir o setor
    def __str__(self):
        """
        Retorna uma representação em string do objeto Gerente, incluindo o setor.
        """
        # Reutilizando a representação da classe base e adicionando o setor.
        informacao_base = super().__str__()
        return f"Gerente| {informacao_base}, Setor: {self._setor}"



# Criando uma instância de Funcionario
funcionario1 = Funcionario("Ana Silva", 3500.00)
funcionario2 = Funcionario("Carlos Pereira", 4200.75)
funcionario3 = Funcionario("João Lima", 2800.00)
funcionario4 = Funcionario("Maria Oliveira", 5000.00)
# Criando uma instância de Gerente
gerente1 = Gerente("Bruno Costa", 12500.50, "Tecnologia")
gerente2 = Gerente("Mariana Souza", 9800.00, "Negócios")

# O uso de print() chama automaticamente o método __str__
print("--- Cadastro de Funcionarios ---")
print(funcionario1)
print(funcionario2)
print(funcionario3)
print("\n--- Cadastro de Gerentes ---")
print(gerente1)
print(gerente2)
