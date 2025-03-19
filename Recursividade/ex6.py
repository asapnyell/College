#Número de Zeros de um número. Escreva uma função recursiva que retorna o número de zeros do
#número informado como parâmetro. Por exemplo se n = 10, a função retorna 1, se n = 10101, a
#função retorna 2

def zeros(x):
    if x == 0:
        return 1
    if x < 10:
        return 0
    
    last_dig = x % 10 # Obtém o último dígito do número
    rest = x // 10 # Remove o último dígito do número