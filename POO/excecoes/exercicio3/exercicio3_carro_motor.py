# Nome do arquivo: exercicio3_carro_motor.py

class Motor:
    """Classe Motor: Valida a potência na criação."""
    
    def __init__(self, potencia):
        if potencia < 1:
            # Levanta a exceção se a regra de negócio for violada
            raise ValueError(f"Potência inválida: {potencia}. Motor deve ter ao menos 1cv.")
            
        self.potencia = potencia
        print(f"Motor de {potencia}cv criado.")

class Carro:
    """Classe Carro: Cria (compõe) um motor internamente."""
    
    def __init__(self, marca, potencia_motor):
        print(f"Iniciando a montagem do {marca}...")
        self.marca = marca
        
        # Tenta criar o motor. 
        # Se Motor() falhar, a exceção vai "parar" a criação do Carro
        # e será propagada para quem tentou criar o Carro.
        self.motor = Motor(potencia_motor)
        
        print(f"{marca} com motor de {self.motor.potencia}cv montado!")

# --- Testando a montagem ---

# Teste 1: Carro válido
print("--- Tentativa 1: Carro Válido ---")
try:
    meu_fusca = Carro("Fusca", 50)
    print("Status: Montagem OK.")

except ValueError as e:
    print(f"Status: Falha na montagem. Causa: {e}")

print("-" * 30)

# Teste 2: Carro com motor inválido (potência 0)
print("--- Tentativa 2: Carro Inválido (0cv) ---")
try:
    minha_bicicleta = Carro("Bicicleta", 0)
    print("Status: Montagem OK.")

except ValueError as e:
    # Captura o ValueError que veio da classe Motor
    print(f"Status: Falha na montagem. Causa: {e}")