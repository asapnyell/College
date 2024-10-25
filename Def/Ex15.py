def mesDoAno(mes):
    meses= ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']

    if mes <1 or mes > 12:
        mes = "Mes invalido"
    else:
        mes = (meses[mes -1])
    return mes
    
mes = int(input("Digite o numero do mes: "))

print(mesDoAno(mes))