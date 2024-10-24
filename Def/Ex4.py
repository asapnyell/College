#Escrever uma função verificarEstacao(dia, mes), que
#retorna qual a estação do ano da data passada por
#parâmetro. Lembrando que a primavera começa no dia
#23 de setembro, o verão em 21 de dezembro, o outono
#em 21 de março e o inverno em 21 de junho.
def qual_estacao (dia, mes):
    if dia < 1 or dia > 31 or mes < 1 or mes > 12:
        return "Data inválida"

    #VERIFICAR ESTAÇÂO DO ANO
    if mes == 9 and dia >= 23 or mes == 10 or mes == 11 \
        or mes == 12 and dia <= 20:
        return"PRIMAVERA"
    else:
        if mes == 12 and dia >= 21 or mes == 1 or mes == 2 \
            or mes == 3 and dia <= 20:
            return "VERAO"
        else:
            if mes == 3 and dia >= 21 or mes == 4 or mes == 5 \
                or mes == 6 and dia <=21:
                return "OUTONO"
            else:
                return "INVERNO"

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
print(qual_estacao(dia, mes))