"""
Crie a classe Funcionario com atributos nome e salario.
Crie a subclasse Gerente, que possui também setor.
Sobrescreva o método __str__ para mostrar todas as informações.

"""
class Funcionario: # Classe base Funcionario
 
    def __init__(self, nome: str, salario: float): # Construtor da classe Funcionario. tipando os parâmetros.
       
        self._nome = nome
        self._salario = salario

    # Sobrescrevendo o método mágico __str__
    def __str__(self):
        """
        Retorna uma representação em string do objeto Funcionario.
        """
        return f"Nome: {self._nome}, Salário: R$ {self._salario:.2f}"


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
        # Chamando o construtor da classe base
        super().__init__(nome, salario)
        self._setor = setor # Atributo específico de Gerente

    # Sobrescrevendo o método mágico __str__ para incluir o setor
    def __str__(self):
        """
        Retorna uma representação em string do objeto Gerente, incluindo o setor.
        """
        # Reutilizando a representação da classe base e adicionando o setor.
        # Removemos 'Funcionário: ' da string da superclasse para maior clareza.
        informacao_base = super().__str__().replace("Funcionário: ", "")
        return f" {informacao_base}, Setor: {self._setor}"


# Criando uma instância de Funcionario
func1 = Funcionario("Ana Silva", 3500.00)
# Criando uma instância de Gerente
gerente1 = Gerente("Bruno Costa", 12500.50, "TI")

# O uso de print() chama automaticamente o método __str__
print(func1)
print(gerente1)
