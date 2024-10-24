#Em uma eleição presidencial existem quatro
# candidatos. Os votos são
#informados através de códigos.
# Os dados utilizados para a contagem dos
#votos obedecem à seguinte codificação:
#1,2,3,4 = voto para os respectivos candidatos;
#5 = voto nulo;
#6 = voto em branco.

print("""Candidato 1 = 1
Candidato 2 = 2
Candidato 3 = 3
Candidato 4 = 4
Voto Nulo = 5
Voto Branco = 6
""")
quantidade_votos1 = 0
quantidade_votos2 = 0
quantidade_votos3 = 0
quantidade_votos4 = 0
quantidade_votos5 = 0
quantidade_votos6 = 0
votos = int(input('Digite o numero do candidato: '))
if votos == 1:
    quantidade_votos1 +=1
if votos == 2:
    quantidade_votos2 += 1
if votos == 3:
    quantidade_votos3 += 1
if votos == 4 :
    quantidade_votos4 += 1
if votos == 5:
    quantidade_votos5 += 1
if votos == 6:
    quantidade_votos6 += 1
while votos >= 1 and votos <= 6:
    votos = int(input('Digite o numero do candidato: '))
    if votos >=1 or votos <=6:
        if votos == 1:
            quantidade_votos1 += 1
        else:
            if votos == 2:
                quantidade_votos2 += 1
            else:
                if votos == 3:
                    quantidade_votos3 += 1
                else:
                    if votos == 4:
                        quantidade_votos4 += 1
                    else:
                        if votos == 5:
                            quantidade_votos5 += 1
                        else:
                            if votos == 6:
                                quantidade_votos6 += 1
print('Total votos Candidato 1=',quantidade_votos1)
print('Total votos Candidato 2=',quantidade_votos2)
print('Total votos Candidato 3=',quantidade_votos3)
print('Total votos Candidato 4=',quantidade_votos4)
print('Total votos Nulos =',quantidade_votos5)
print('Total votos Brancos=',quantidade_votos6)