#Calcular o aumento que sera dado a um funcionario
#salario atual, porcentagem do aumento, apresentar novo valor do salario e o valor do aumento
print("Calculo aumento salario")
salario_atual=float(input("Digite seu salario atual: "))
porcentagem_aumento=float(input("Digite a porcentagem de aumento: "))
#
#convertendo a porcentagem para decimal
aumento_decimal = porcentagem_aumento/100
#
#calculo valor do aumento
valor_aumento = salario_atual * aumento_decimal
#
#calculo novo salario
novo_salario = salario_atual + valor_aumento
print(" O valor do aumento é de: ",valor_aumento)
print("O novo salario é de: ",novo_salario)