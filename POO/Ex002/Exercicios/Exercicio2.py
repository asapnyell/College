# Definindo a classe base Funcionario
class Funcionario:
    """
    Classe base para representar um funcionário genérico.
    """
    def __init__(self, nome: str, salario: float):
        """
        Construtor da classe Funcionario. tipando os parâmetros.
        """
        self._nome = nome
        # Boas práticas: Armazenar valores monetários como float ou Decimal
        self._salario = salario

    # Sobrescrevendo o método mágico __str__
    def __str__(self):
        """
        Retorna uma representação em string do objeto Funcionario.
        """
        # Formatando o salário para melhor visualização
        salario_formatado = f"R${self._salario:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        return f"Funcionário: {self._nome}, Salário: {salario_formatado}"


# Definindo a subclasse Gerente, que herda de Funcionario
class Gerente(Funcionario):
    """
    Classe que representa um Gerente, herdando de Funcionario.
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
        base_str = super().__str__().replace("Funcionário: ", "")
        return f"Gerente: {base_str}, Setor: {self._setor}"


# --- Teste do Exercício 2 ---
print("\n--- Teste do Exercício 2 (Funcionário) ---")
func1 = Funcionario("Ana Silva", 3500.00)
gerente1 = Gerente("Bruno Costa", 12500.50, "TI")

# O uso de print() chama automaticamente o método __str__
print(func1)
print(gerente1)
