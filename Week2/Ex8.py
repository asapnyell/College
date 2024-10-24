#Faça a leitura do ano atual e do ano de nascimento de uma pessoa e
#exibir sua idade. A seguir, informe se a pessoa é bebê (0 a 3 anos),
#criança (4 a 11 anos), adolescente (12 a 17 anos), adulta (18 a 64 anos)
#ou idosa (65 anos em diante).
ano_nascimento = int(input("Qual ano de nascimento: "))
ano_atual = 2024
idade = ano_atual - ano_nascimento
if idade >-1 and idade <=3:
    print(idade,"Bebe")
elif idade >3 and idade <=11:
    print(idade,"Crianca")
elif idade >11 and idade <=17:
    print("Adolescente")
elif idade >17 and idade <=64:
    print("Adulta")
else:
    print("Idoso")