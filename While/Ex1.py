# . A prefeitura de uma cidade fez uma pesquisa entre seus
# habitantes, coletando dados sobre o salário e número de filhos.
# A prefeitura deseja saber:
# a) média do salário da população;
# b) média do número de filhos;
# c) maior salário;
# d) percentual de pessoas com salário até R$1000,00.
# O final da leitura de dados se dará com a entrada de um salário
# negativo
soma_salario = 0
quantidade = 0
soma_filhos = 0
salario_ate_mil = 0
salario = int(input('Digite o valor: '))
if salario_ate_mil >=0 and salario_ate_mil <=1000:
    salario_ate_mil += 1
maior_salario = salario
menor_salario = salario
while salario >=0:
    soma_salario += salario
    quantidade += 1
    filhos = int(input('Digite numero de filhos: '))
    if filhos == 0:
        soma_filhos
    if filhos > 0:
        soma_filhos = soma_filhos + filhos
    salario = int(input('Digite o valor: '))
    if salario_ate_mil >= 0 and salario_ate_mil <= 1000:
        salario_ate_mil += 1
    if salario > maior_salario:
        maior_salario = salario
    if salario < menor_salario and salario >=0:
        menor_salario = salario
media_salario = soma_salario / quantidade
media_filhos = soma_filhos / quantidade
media_salario_ate_mil = salario_ate_mil / quantidade
print('Media Salario=',media_salario)
print('Media Filhos=',media_filhos)
print('Maior salario=',maior_salario)
print('Menor salario=',menor_salario)
print('Media pessoal salario ate mil=', media_salario_ate_mil)

print('FIM')
