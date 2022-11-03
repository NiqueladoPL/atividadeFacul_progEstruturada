valores = input()
a = float(valores.split()[0])
b = float(valores.split()[1])
c = float(valores.split()[2])

delta = (b ** 2) - 4 * a * c

if (a == 0) or (delta < 0):
    print("Impossivel calcular")
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)
    print("R1 = {:.5f}".format(x1))
    print("R2 = {:.5f}".format(x2))
