a = input()
a1 = int(a.split()[0])
a2 = int(a.split()[1])
a3 = float(a.split()[2])

b = input()
b1 = int(b.split()[0])
b2 = int(b.split()[1])
b3 = float(b.split()[2])

valor_final = (a2 * a3) + (b2 * b3)

print("VALOR A PAGAR: R$ {:.2f}".format(valor_final))
