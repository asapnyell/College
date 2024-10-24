quilowatts_consumidos = float(input("Digite o número de quilowatts consumidos: "))
valor_por_quilowatt = 0.12  # Valor por quilowatt em reais
valor_total = quilowatts_consumidos * valor_por_quilowatt
icms = valor_total * 0.18
valor_final = valor_total + icms
print("Valor total a ser pago (com ICMS): ", valor_final)