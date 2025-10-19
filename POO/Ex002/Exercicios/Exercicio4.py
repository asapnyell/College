"""
Crie duas classes: Nadador (com método nadar()) e Corredor (com método correr()).
Depois, crie a classe Triatleta herdando das duas e testando os métodos.

"""

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

    def competir(self): # método que executa as três ações do Triatleta

        print("\nIniciando a competição de Triatlo:")
        self.nadar()
        self.pedalar()
        self.correr()
        print("Triatlo concluído!")

# Testando a classe Triatleta
triatleta1 = Triatleta()

print("Testando os métodos herdados e o próprio do Triatleta:")
triatleta1.nadar()   # Método herdado de Nadador
triatleta1.correr()  # Método herdado de Corredor
triatleta1.pedalar() # Método próprio de Triatleta

triatleta1.competir()
