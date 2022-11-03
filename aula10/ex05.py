print("Insira dois valores maiores que zero para serem somados, ex:(45 12)")
valores = input("-> ")
valSplit = valores.split()

x = int(valSplit[0])
y = int(valSplit[1])

while (x < 1) or (y < 1):
    if x < 1:
        print("Valor ({}) incorreto, insira um valor válido (maior que 0)".format(x))
        x = int(input("->"))
    elif y < 1:
        print("Valor ({}) incorreto, insira um valor válido (maior que 0)".format(y))
        y = int(input("->"))

print("A soma de {} + {} é igual a: {}".format(x, y, (x + y)))
