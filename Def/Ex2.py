#Faça uma função que recebe por parâmetro o raio de
#uma esfera e calcule o seu volume (v = (4 x pi x R3)/3).

def calculo_volume(raio):
    volume = (4 * 3.14 * raio * raio * raio) /3
    return volume

raio = int(input("Digite o valor do raio: "))
total_volume = calculo_volume(raio)
print(total_volume)