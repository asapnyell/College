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