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
