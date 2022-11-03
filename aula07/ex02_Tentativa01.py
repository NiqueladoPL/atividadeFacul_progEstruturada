# Faça um sistema que, dado um valor em reais, informe a menor quantidade de cédulas necessárias que acumulem esse valor.

valor = int(input("Valor em reais: "))

notasCem = int(valor / 100)
a = notasCem * 100

notasCinquenta = int((valor - a) / 50)
b = notasCinquenta * 50

notasVinte = int((valor - (a + b)) / 20)
c = notasVinte * 20

notasDez = int((valor - (a + b + c)) / 10)
d = notasDez * 10

notasCinco = int((valor - (a + b + c + d)) / 5)
e = notasCinco * 5

notasDois = int((valor - (a + b + c + d + e)) / 2)

print("Notas 100: " + str(notasCem))
print("Notas 50: " + str(notasCinquenta))
print("Notas 20: " + str(notasVinte))
print("Notas 10: " + str(notasDez))
print("Notas 5: " + str(notasCinco))
print("Notas 2: " + str(notasDois))
