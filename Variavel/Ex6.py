#Calculo salario liquido
salario_bruto = float(input("Digite seu salario bruto: "))
horas_ex = float(input("Digite o numero de horas trabalhadas: "))
total_hex = horas_ex * 2
inss = 0.08
salario_liquido = salario_bruto + total_hex
totalsl = salario_liquido - inss
print("Valor total das horas extras é de: ",total_hex, "R$")
print("O salario liquido é: ", totalsl)
