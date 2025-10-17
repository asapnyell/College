"""
Crie a classe Animal com o método falar().
Crie as subclasses Gato, Cachorro e Vaca, cada uma sobrescrevendo falar() com seu som característico.
Instancie os animais e teste o polimorfismo.

"""
class Animal: #  classe base Animal
 
    def falar(self):
        pass  # Método vazio, que será sobrescrito nas subclasses.


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

# Instanciando os animais
gato = Gato()
cachorro = Cachorro()
vaca = Vaca()

# Criando uma lista de animais (exemplo de como o polimorfismo é usado)
animais = [gato, cachorro, vaca]

# O loop chama o método 'falar()' de cada objeto na lista,
# mas o comportamento é diferente para cada tipo de animal (Polimorfismo)
for animal in animais:
    print(f"O som do {animal.__class__.__name__} é: {animal.falar()}") # Usando __class__.__name__ para obter o nome da classe de cada objeto 
    # animal.falar() chamará a implementação correta de cada objeto (Miau, Au Au, Muuu)

