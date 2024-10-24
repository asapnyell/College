#Crie um programa que solicita ao usuário
#a entrada de 5 notas e calcula
# a média dessas notas.

def media_notas(n1, n2, n3, n4, n5):
    media = (n1+n2+n3+n4+n5)/5
    return media
n1 = int(input("Digte a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))
n4 = int(input("Digite a quarta nota: "))
n5 = int(input("DIgite a quinta nota: "))

media_total = media_notas(n1,n2,n3,n4,n5)
print(media_total)