#Faça uma função que recebe a média final de um aluno
#por parâmetro e retorna o seu conceito, conforme a
#tabela abaixo:

#Nota Conceito
#De 0 a 49 D
#De 50 a 69 C
#De 70 a 89 B
#De 90 a 100 A

def calculo_media(port, mat, infor):
    media = (port + mat + infor) /3

    if media >= 0 and media <= 49:
         conceito = "CONCEITO D"
    else:
        if media >= 50 and media <=69:
            conceito = "CONCEITO C"
        else:
            if media >= 70 and media <=89:
                conceito = "CONCEITO B"
            else:
                conceito = "CONCEITO A"
    return media, conceito
port = int(input("Digite a nota de port: "))
mat = int(input("Digite a nota de mat: "))
infor = int(input("Digite a nota de info: "))
media, conceito = calculo_media(port, mat, infor)
print("CONCEITO:" ,conceito)
print("MEDIA: ",media)