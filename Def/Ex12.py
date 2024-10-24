# 4. A prefeitura de uma cidade fez uma pesquisa entre seus
# habitantes, coletando dados sobre o salário e número de filhos.
# A prefeitura deseja saber:
# a) média do salário da população;
# b) média do número de filhos;
# c) maior salário;
# d) percentual de pessoas com salário até R$1000,00.
# O final da leitura de dados se dará com a entrada de um salário
# negativo

def media_salario_efilhos():
    salario = float(input("Digite seu salario: "))
    if salario > 0:
        maior = salario
        menor = salario
        rodada = 1
        totalfilhos = 0
        total_salario = salario
        salario_atemil = 0
        if salario <= 1000:
            salario_atemil += 1
        filhos = int(input("Digite a quantidade de filhos: "))
        if filhos > 0:
            totalfilhos += filhos
        while salario > 0:
            salario = float(input("Digite seu salario: "))
            if salario > 0:
                if salario > maior:
                    maior = salario
                if salario < menor:
                    menor = salario
                rodada += 1
                total_salario += salario
                if salario <= 1000:
                    salario_atemil += 1
                filhos = int(input("Digite a quantidade de filhos: "))
                if filhos > 0:
                    totalfilhos += filhos
        media = total_salario / rodada
        media_filhos = totalfilhos / rodada
        salario_atemil = (salario_atemil / rodada) * 0.10
        return media, media_filhos, maior, menor,salario_atemil

media_salario, media_filhos, maior, menor,salario_atemil = media_salario_efilhos()
print(f"Media de salario é = R${media_salario}\nA media de filhos é {media_filhos}\n"
      f"Maior salario é {maior}\nMenor salario {menor}\nPercentual de salario ate mil é {salario_atemil:.2f}%")