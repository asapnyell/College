# 18) Função para verificar número primo
import math


print("Função para verificar se um número é primo.")
def eh_primo(n):
    if n < 2: # Números menores ou iguais a 1, por definição, não são primos.
        return False
    for i in range(2, int(math.sqrt(n)) + 1): 
        if n % i == 0:
            return False
    return True

raiz_quadrada = math.sqrt(7)
print(raiz_quadrada)
print("100 é primo?", eh_primo(100))
print("97 é primo?", eh_primo(97))