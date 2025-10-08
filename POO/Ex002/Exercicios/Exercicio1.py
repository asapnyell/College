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



carro1 = Carro("Ford", 2022, 4)
carro2 = Carro("Chevrolet", 2006, 2)
moto1 = Moto("Honda", 2023, 150)
moto2 = Moto("Yamaha", 2020, 300)

print("\nDetalhes do Carro:")
carro1.detalhes()
carro2.detalhes()

print("\nDetalhes da Moto:")
moto1.detalhes()
moto2.detalhes()
