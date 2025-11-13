# Nome do arquivo: exercicio2_calculadora.py

class Calculadora:
    
    def dividir(self, a_str, b_str):
        """Tenta dividir dois números vindos como string."""
        
        try:
            # Tenta converter (pode dar ValueError)
            a_num = int(a_str)
            b_num = int(b_str)
            
            # Tenta dividir (pode dar ZeroDivisionError)
            resultado = a_num / b_num

        except ValueError:
            print("Erro: As entradas devem ser números válidos.")
            
        except ZeroDivisionError:
            print("Erro: Não é possível dividir por zero.")
            
        else:
            # Executa APENAS se não houver exceção
            print(f"Resultado da divisão de {a_num} por {b_num}: {resultado:.2f}")
            
        finally:
            # Executa SEMPRE (com ou sem exceção)
            print("Operação encerrada.")

# --- Testando a calculadora ---
calculadora = Calculadora()

print("--- Teste 1: Sucesso ---")
calculadora.dividir("100", "5")

print("\n--- Teste 2: Erro de Valor ---")
calculadora.dividir("cem", "cinco")

print("\n--- Teste 3: Divisão por Zero ---")
calculadora.dividir("100", "0")