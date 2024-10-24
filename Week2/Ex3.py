#Efetuar a leitura de uma nota e, se o valor for
# maior ou igual a 60, imprimir
#na tela &quot;APROVADO&quot;, se for menor,
# imprimir reprovado. Testar ainda se
#o valor lido foi maior do que 100 ou menor do que zero. Neste caso,
#imprimir &;NOTA INVÁLIDA&quot;.

nota = int(input("Digite a nota: "))
if nota >100:
    print("Nota Invalida")
elif  nota <0:
    print("Nota invalida")
elif nota >= 60:
    print("Aprovado")
else:
     print("Reprovado")