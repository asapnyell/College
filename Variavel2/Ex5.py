#Ler um número inteiro e testar se o valor lido termina com
# 0 (divisível por
#10). Em caso positivo, exiba a metade deste número. Caso contrário,
#exibir a mensagem &quot;O número digitado não termina com 0&quot;.

numero = int(input("Digite o numero: "))
if numero % 10 == 0:
    print(numero / 2 )
else:
    print("Numero digitado nao termina com 0")