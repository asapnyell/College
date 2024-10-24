#Faça a leitura do salário atual e do tempo de serviço
# de um funcionário. A
#seguir, calcule o seu salário reajustado. Funcionários com até 1 ano de
#empresa, receberão aumento de 10%. Funcionários com mais de um ano
#de tempo de serviço, receberão aumento de 20%.

salario_atual = float(input("Digite seu salario: "))
tempo_servico = float(input("Quantos anos de servico: "))
reajuste1 = salario_atual*0.10
reajuste2 = salario_atual*0.20
if tempo_servico <= 1:
    print("Seu salario é", reajuste1 + salario_atual)
elif tempo_servico >1:
    print("Seu salario é ",reajuste2+ salario_atual )