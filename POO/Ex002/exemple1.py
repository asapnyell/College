# Definindo a classe base Veiculo
class Veiculo: # Classe base para representar um veículo genérico.

    def __init__(self, marca: str, ano: int): 
        """
        Construtor da classe Veiculo, que inicializa os atributos básicos e estou tipando os parâmetros.

        """
        # Boas práticas: Atributos privados ou protegidos (usamos o padrão 'protegido' com _ )
        # A boa prática em Python para atributos públicos/propriedades é o uso direto,
        #  aqui usei o _ para demonstrar a intenção de uso interno.
        self._marca = marca
        self._ano = ano

    def detalhes(self):
        """
        Método que exibe as informações básicas do veículo.
        """
        print(f"Marca: {self._marca}, Ano: {self._ano}")


# Definindo a subclasse Carro, que herda de Veiculo
class Carro(Veiculo):
    """
    Classe que representa um Carro, herdando de Veiculo.
    Possui o atributo específico 'portas'.
    """
    def __init__(self, marca: str, ano: int, portas: int):
        """
        Construtor da classe Carro.

        """
        # Chamando o construtor da classe base (Veiculo)
        super().__init__(marca, ano)
        self._portas = portas # Atributo específico de Carro

    # Sobrescrevendo/Estendendo o método detalhes()
    def detalhes(self):
        """
        Método que exibe as informações do carro, incluindo o número de portas.
        """
        # Chamando o método da classe base para exibir as informações comuns
        super().detalhes()
        print(f"Tipo: Carro, Portas: {self._portas}")


# Definindo a subclasse Moto, que herda de Veiculo
class Moto(Veiculo):
    """
    Classe que representa uma Moto, herdando de Veiculo.
    Possui o atributo específico 'cilindrada'.
    """
    def __init__(self, marca: str, ano: int, cilindrada: int):
        """
        Construtor da classe Moto.
        """
        # Chamando o construtor da classe base (Veiculo)
        super().__init__(marca, ano)
        self._cilindrada = cilindrada # Atributo específico de Moto

    # Sobrescrevendo/Estendendo o método detalhes()
    def detalhes(self):
        """
        Método que exibe as informações da moto, incluindo a cilindrada.
        """
        # Chamando o método da classe base
        super().detalhes()
        print(f"Tipo: Moto, Cilindrada: {self._cilindrada}cc")


# --- Teste do Exercício 1 ---
print("--- Teste do Exercício 1 (Veículo) ---")
carro1 = Carro("Ford", 2022, 4)
moto1 = Moto("Honda", 2023, 150)

print("\nDetalhes do Carro:")
carro1.detalhes()

print("\nDetalhes da Moto:")
moto1.detalhes()
print("-" * 35)



## Exercício 2 – Funcionário
""""
Este exercício demonstra o conceito de **Herança** e **Sobrescrita de Métodos** através das classes `Funcionario` (base) e `Gerente` (subclasse).
"""

# Definindo a classe base Funcionario
class Funcionario:
    """
    Classe base para representar um funcionário genérico.
    """
    def __init__(self, nome: str, salario: float):
        """
        Construtor da classe Funcionario.

        :param nome: O nome do funcionário.
        :param salario: O salário do funcionário.
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

        :param nome: O nome do gerente.
        :param salario: O salário do gerente.
        :param setor: O setor que o gerente administra.
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
print("-" * 35)

"""""

## Exercício 3 – Animais

Este exercício demonstra o conceito de **Polimorfismo** (muitas formas) através da sobrescrita do método `falar()` em classes que herdam de uma classe base (`Animal`).

```python
"""""
# Definindo a classe base Animal
class Animal:
    """
    Classe base para representar um animal genérico.
    """
    def falar(self):
        """
        Método genérico para o som do animal.
        Deve ser sobrescrito pelas subclasses.
        """
        # Boas Práticas: Levantar um erro ou retornar uma mensagem genérica
        raise NotImplementedError("O método 'falar' deve ser sobrescrito nas subclasses.")


# Subclasse Gato
class Gato(Animal):
    """
    Classe Gato que sobrescreve o método falar().
    """
    def falar(self):
        return "Miau!"


# Subclasse Cachorro
class Cachorro(Animal):
    """
    Classe Cachorro que sobrescreve o método falar().
    """
    def falar(self):
        return "Au Au!"


# Subclasse Vaca
class Vaca(Animal):
    """
    Classe Vaca que sobrescreve o método falar().
    """
    def falar(self):
        return "Muuu!"


# --- Teste do Exercício 3 ---
print("\n--- Teste do Exercício 3 (Animais - Polimorfismo) ---")
# Instanciando os animais
gato = Gato()
cachorro = Cachorro()
vaca = Vaca()

# Criando uma lista de animais (exemplo de como o polimorfismo é usado)
animais = [gato, cachorro, vaca]

# O loop chama o método 'falar()' de cada objeto na lista,
# mas o comportamento é diferente para cada tipo de animal (Polimorfismo)
for animal in animais:
    # animal.falar() chamará a implementação correta (Miau, Au Au, Muuu)
    print(f"O som do {animal.__class__.__name__} é: {animal.falar()}")
print("-" * 35)


## Exercício 4 – Herança Múltipla


# Definindo a classe Nadador
class Nadador:
    """
    Classe que representa a capacidade de nadar.
    """
    def nadar(self):
        """
        Método que simula a ação de nadar.
        """
        print("Nadando na água...")


# Definindo a classe Corredor
class Corredor:
    """
    Classe que representa a capacidade de correr.
    """
    def correr(self):
        """
        Método que simula a ação de correr.
        """
        print("Correndo na pista...")


# Definindo a classe Triatleta, que herda de Nadador E Corredor (Herança Múltipla)
class Triatleta(Nadador, Corredor):
    """
    Classe que representa um Triatleta, herdando as habilidades de
    Nadador e Corredor.
    """
    def pedalar(self):
        """
        Método específico do Triatleta.
        """
        print("Pedalando na estrada...")

    # Opcional: Um método que executa as três ações
    def competir(self):
        """
        Executa todas as ações de um triatlo.
        """
        print("\nIniciando a competição de Triatlo:")
        self.nadar()
        self.pedalar()
        self.correr()
        print("Triatlo concluído!")


# --- Teste do Exercício 4 ---
print("\n--- Teste do Exercício 4 (Herança Múltipla) ---")
triatleta1 = Triatleta()

print("Testando os métodos herdados e o próprio:")
triatleta1.nadar()   # Método herdado de Nadador
triatleta1.correr()  # Método herdado de Corredor
triatleta1.pedalar() # Método próprio de Triatleta

triatleta1.competir()
print("-" * 35)