#Escrever uma função calcularQuociente(dividendo,
#divisor), que retorna a divisão inteira (sem casas
#decimais) de dividendo por divisor e outra função
#calcularResto(dividendo, divisor) que retorna o
#resto.
def calcular_quociente(dividendo , divisor):
    if divisor == 0:
        return "INVALIDO DIVISAO POR 0"
    return dividendo // divisor
def calcular_resto (dividendo, divisor):
    if divisor == 0:
        return "INVALIDO DIVISAO POR 0"
    return dividendo % divisor
dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))
quociente = calcular_quociente(dividendo, divisor)
resto = calcular_resto(dividendo, divisor)
print('QUOCIENTE =',quociente)
print('RESTO =' ,resto)