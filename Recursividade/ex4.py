#Potência com Recursão. #Escreva uma função #recursiva que retorna o #valor da potência de #base b e
#expoente n, informados como parâmetros

def pow(b,n):
    if n == 0:
        return 1
    elif n < 0:
        return 1/pow(b,-n)
    return b*pow(b,n-1)

print(pow(10,5))