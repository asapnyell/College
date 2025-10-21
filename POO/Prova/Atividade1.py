"""
Recebe a temperatura em Celsius no construtor;
Possui um método converter_para_fahrenheit() que retorna o valor convertido;
Possui outro método avaliar_clima() que imprime:
“Está frio” se for menor que 15°C
“Temperatura agradável” se estiver entre 15°C e 30°C
“Está quente” se for maior que 30°C.
Crie duas instâncias com temperaturas diferentes e teste os métodos.

"""
class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius  # Armazena a temperatura em Celsius no objeto.

    def converter_para_fahrenheit(self):
        fahrenheit = (self.celsius * 9/5) + 32 # Acessa a temperatura em Celsius do próprio objeto.
        return f"Graus fahrenheit: {fahrenheit:.2f}"

    def avaliar_clima(self):
        if self.celsius < 15:
            print("Está frio")
        elif 15 <= self.celsius <= 30:
            print("Temperatura agradável")
        else:
            print("Está quente")

# Criando uma instância da classe `Temperatura` com 2 graus Celsius.
temperatura1 = Temperatura(celsius=2)
temperatura2 = Temperatura(celsius=20)


# Testando os métodos
temperatura1 = Temperatura(celsius=2)
print(temperatura1.converter_para_fahrenheit())

temperatura2 = Temperatura(celsius=20)
print(temperatura2.converter_para_fahrenheit())