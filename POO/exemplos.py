# 7) Maior entre três números
print("Encontrar o maior número entre três números.")
primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))
terceiro_numero = int(input("Digite o terceiro número: "))

def maior_de_tres(numero_primeiro, numero_segundo, numero_terceiro):
    if numero_primeiro >= numero_segundo and numero_primeiro >= numero_terceiro:
        return numero_primeiro
    elif numero_segundo >= numero_primeiro and numero_segundo >= numero_terceiro:
        return numero_segundo
    else:
        return numero_terceiro

maior = maior_de_tres(primeiro_numero, segundo_numero, terceiro_numero)
print(f"O maior número é: {maior}")