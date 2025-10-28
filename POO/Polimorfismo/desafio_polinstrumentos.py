from abc import ABC, abstractmethod

# --- 1. Classe Abstrata (Superclasse) ---
# Define o "contrato" que todos os instrumentos devem seguir.
# Qualquer classe que herdar de InstrumentoMusical DEVE implementar o método tocar().

class InstrumentoMusical(ABC):
    """
    Classe abstrata que serve como base para todos os instrumentos.
    Força a implementação do método tocar() e fornece um método
    afinar() padrão que pode ser sobrescrito.
    """
    
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def tocar(self):
        """
        Método abstrato para reproduzir o som do instrumento.
        Deve ser sobrescrito por todas as subclasses.
        """
        pass

    def afinar(self):
        """
        Método concreto (opcional) que pode ser usado ou sobrescrito.
        Define um comportamento padrão para afinação.
        """
        print(f"Afinando o(a) {self.nome} (som genérico de afinação)...")


# --- 2. Subclasses (Classes Concretas) ---
# Cada classe representa um instrumento específico e herda de InstrumentoMusical.
# Elas OBRIGATORIAMENTE sobrescrevem (override) o método tocar().

class Violao(InstrumentoMusical):
    """Representa um Violão."""
    
    def __init__(self):
        # Chama o construtor da classe pai (InstrumentoMusical)
        super().__init__("Violão")

    def tocar(self):
        """Sobrescrita criativa do método tocar."""
        print(f"{self.nome}: 🎸 'Strumming chords'... Soando um belo dedilhado clássico.")

    def afinar(self):
        """Sobrescrita opcional do método afinar."""
        print(f"{self.nome}: Girando as tarraxas... 'Tlim... tlim... TLOIM'. Afinado!")

class Piano(InstrumentoMusical):
    """Representa um Piano."""
    
    def __init__(self):
        super().__init__("Piano")

    def tocar(self):
        """Sobrescrita criativa do método tocar."""
        print(f"{self.nome}: 🎹 'Plin plin plon'... Tocando uma sonata de Beethoven.")
    
    # Nota: O Piano usará o método afinar() padrão da classe pai.

class Bateria(InstrumentoMusical):
    """Representa uma Bateria."""
    
    def __init__(self):
        super().__init__("Bateria")

    def tocar(self):
        """Sobrescrita criativa do método tocar."""
        print(f"{self.nome}: 🥁 'BADUM-TSS!'... Mantendo o ritmo da banda.")
    
    def afinar(self):
        """Sobrescrita opcional do método afinar."""
        print(f"{self.nome}: Apertando os parafusos da pele... 'Tum... Tum...'. Pronto!")

class Saxofone(InstrumentoMusical):
    """Representa um Saxofone."""
    
    def __init__(self):
        super().__init__("Saxofone")

    def tocar(self):
        """Sobrescrita criativa do método tocar."""
        print(f"{self.nome}: 🎷 'Fooooommmm'... Aquele solo de jazz suave.")

    def afinar(self):
        """Sobrescrita opcional do método afinar."""
        print(f"{self.nome}: Ajustando a palheta e aquecendo... 'Fuuu'.")

class Violino(InstrumentoMusical):
    """Representa um Violino."""
    
    def __init__(self):
        super().__init__("Violino")

    def tocar(self):
        """Sobrescrita criativa do método tocar."""
        print(f"{self.nome}: 🎻 'Ziiiiim'... Notas altas e emocionantes da orquestra.")

    def afinar(self):
        """Sobrescrita opcional do método afinar."""
        print(f"{self.nome}: Apertando as cravelhas e usando o microafinador...")


# --- 3. Funções Polimórficas ---
# Estas funções recebem uma lista de objetos (InstrumentoMusical)
# e chamam o mesmo método (tocar ou afinar) em cada um,
# mas o comportamento exato depende do TIPO do objeto.

def executar_show(instrumentos: list[InstrumentoMusical]):
    """
    Função polimórfica principal.
    Recebe uma lista de instrumentos e chama o método tocar() de cada um.
    Não importa qual é o instrumento (Violao, Piano, etc.),
    desde que ele "assine o contrato" de InstrumentoMusical.
    """
    print("\n--- 🎶 O SHOW VAI COMEÇAR! 🎶 ---")
    for instrumento in instrumentos:
        # A mágica do polimorfismo acontece aqui:
        # O Python sabe qual método tocar() chamar (o do Violao, o do Piano, etc.)
        instrumento.tocar()
    print("--- 🎶 Show finalizado! Aplausos! 🎶 ---")


def preparar_orquestra(instrumentos: list[InstrumentoMusical]):
    """
    Função extra de desafio (também polimórfica).
    Prepara os instrumentos antes do show, chamando afinar() de cada um.
    """
    print("--- Preparando os instrumentos antes do show ---")
    for instrumento in instrumentos:
        # Outra chamada polimórfica!
        instrumento.afinar()
    print("--- Instrumentos prontos! ---")


# --- 4. Execução Principal do Programa ---
# Bloco que será executado quando o script for rodado.

if __name__ == "__main__":
    
    # 1. Criar os "músicos" (objetos de cada subclasse)
    meu_violao = Violao()
    meu_piano = Piano()
    minha_bateria = Bateria()
    meu_sax = Saxofone()
    meu_violino = Violino()

    # 2. Montar a orquestra (uma lista de objetos InstrumentoMusical)
    orquestra = [meu_violao, meu_piano, minha_bateria, meu_sax, meu_violino]

    # 3. Chamar a função extra (preparar/afinar)
    preparar_orquestra(orquestra)

    # 4. Chamar a função polimórfica principal
    executar_show(orquestra)

    # Teste de flexibilidade: e se for um show "solo"?
    # A mesma função funciona com apenas um item.
    # executar_show([meu_sax])


# --- 5. Desafio Reflexivo (Opcional) ---

"""
P: “Por que o polimorfismo é importante em sistemas orientados a objetos? 
    Cite um exemplo prático do mundo real em que ele seria útil.”

R: O polimorfismo é crucial porque permite que tratemos objetos de classes 
diferentes (mas que compartilham uma superclasse ou interface comum) 
de maneira uniforme. Isso torna o código muito mais flexível, extensível 
e limpo. Em vez de escrever um 'if' para cada tipo de objeto 
(ex: se for violão, faça X; se for piano, faça Y), podemos 
simplesmente chamar o mesmo método (ex: instrumento.tocar()) e deixar 
que o próprio objeto decida como executar a ação.

Exemplo prático: Um sistema de e-commerce com diferentes métodos de 
pagamento (CartaoDeCredito, Boleto, Pix). Todos podem herdar de uma 
classe 'MetodoPagamento' e implementar um método 'processar_pagamento()'. 
O carrinho de compras não precisa saber os detalhes de cada um; ele 
apenas chama 'pagamento.processar_pagamento()' e o polimorfismo 
garante que a lógica correta (seja validar o cartão ou gerar o QR Code 
do Pix) seja executada.
"""