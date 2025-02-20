#Escrever uma Função Recursiva para calcular o
# máximo divisor comum de dois números dados como parâmetros.
# Sabe-se que o MDC de dois números naturais não nulos x e
# y é dado por 

def MDC(x,y):
    if x == y:
        return x
    elif x > y:
        return MDC(x-y,y)
    return MDC(y ,x)

print(MDC(100,34))