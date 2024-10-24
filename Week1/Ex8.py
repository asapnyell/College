#Calcular a média de combustível gasto pelo usuário, sendo informado a
#quantidade de quilômetros rodados e a quantidade de combustível
#consumido.
kmr = float(input("informe quantos km rodados: "))
qc = float(input("Digite qauntidade de combustivel: "))
#calculo media
media_consumo = kmr / qc
print("A média de combustível gasto é de:", media_consumo, "km/l")