meses = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
mes = int(input("Digite o numero do mes: "))

if mes <1 or mes >12:
        print("Mes invalido")
else:
    print(meses[mes - 1])