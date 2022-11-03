# Faça um sistema que, dado um valor em reais, informe a menor quantidade de cédulas necessárias que acumulem esse valor.
# Cédulas de 100, 50, 20, 10, 5 e 2.

valor = int(input("Valor em reais: "))

total = valor

while total >= 100:
    total = total - 100
    n100 = n100 + 1

while total >= 50:
    total = total - 50
    n50 = n50 + 1

while total >= 20:
    total = total - 20
    n20 = n20 + 1

while total >= 10:
    total = total - 10
    n10 = n10 + 1

while total >= 5:
    total = total - 5
    n5 = n5 + 1

while total >= 100:
    total = total - 100
    n2 = n2 + 1

print("Notas 100: " + str(n100))
print("Notas 50: " + str(n50))
print("Notas 20: " + str(n20))
print("Notas 10: " + str(n10))
print("Notas 5: " + str(n5))
print("Notas 2: " + str(n2))
