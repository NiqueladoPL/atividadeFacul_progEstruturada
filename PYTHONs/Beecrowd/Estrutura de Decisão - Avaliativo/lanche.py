num = input()
cod = int(num.split()[0])
qtd = int(num.split()[1])

if cod == 1:
    total = (4.00 * qtd)
elif cod == 2:
    total = (4.50 * qtd)
elif cod == 3:
    total = (5.00 * qtd)
elif cod == 4:
    total = (2.00 * qtd)
elif cod == 5:
    total = (1.50 * qtd)

print("Total: R$ {:.2f}".format(total))