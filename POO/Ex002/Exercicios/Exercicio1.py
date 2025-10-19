"""
Crie a classe Veiculo com atributos marca e ano.
Depois crie as subclasses Carro e Moto, cada uma com um atributo específico.
Faça um método detalhes() que exibe as informações.

"""
class Veiculo: # Classe base para representar um veículo genérico.

    def __init__(self, marca: str, ano: int): # Construtor da classe Veiculo, que inicializa os atributos básicos e estou tipando os parâmetros.

         # Usei atributo 'protegido' com _ . Para indicar que não devem ser acessados diretamente fora da classe ou suas subclasses.

        self._marca = marca 
        self._ano = ano
       

    def detalhes(self): # Método que exibe as informações básicas do veículo.
       print(f"Marca: {self._marca}, Ano: {self._ano}")


# Definindo a subclasse Carro, que herda de Veiculo
class Carro(Veiculo):
    """
    Classe que representa um Carro, herdando de Veiculo.
    Possui o atributo específico 'portas'.
    """
    # Construtor da classe Carro.
    def __init__(self, marca: str, ano: int, portas: int):
       
        # Chamando o construtor da classe base (Veiculo)
        super().__init__(marca, ano)
        self._portas = portas # Atributo específico de Carro

    # Sobrescrevendo/Estendendo o método detalhes()
    def detalhes(self):
        """
        Método que exibe as informações do carro, incluindo o número de portas.
        """
        # Chamando o método da classe base para exibir as informações comuns
        print(f"Tipo: Carro, Marca: {self._marca}, Ano: {self._ano}, Portas: {self._portas}")


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
        print(f"Tipo: Moto, Marca: {self._marca}, Ano: {self._ano}, Cilindrada: {self._cilindrada}cc")



carro1 = Carro("Ford", 2022, 4)
carro2 = Carro("Chevrolet", 2006, 2)
moto1 = Moto("Honda", 2023, 150)
moto2 = Moto("Yamaha", 2020, 300)

print("\nDetalhes dos Veículos:")
carro1.detalhes()
carro2.detalhes()

print("\n")
moto1.detalhes()
moto2.detalhes()
