#Escrever a função que recebe por parâmetro uma string e um número. A
#função deve retornar os primeiros caracteres da string de acordo com o
#número passado por parâmetro.

def retorno_carac(palavra,numero):
    situacao = ""
    for i in range(numero):
        situacao += palavra[i]
    return situacao
palavra = str(input("Digite uma palavra: "))
numero = int(input("Quantos caracteres quer exibir da palavra: "))
print(retorno_carac(palavra, numero))