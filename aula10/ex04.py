n = int(input("Insira a quantidade de valores a serem lidos: "))

dentro = 0
fora = 0
acc = 0

while acc < n:
    x = int(input("Insira um valor: "))

    if (x >= 10) and (x <= 20):
        dentro += 1
    else:
        fora += 1

    acc += 1

print("{} in".format(dentro))
print("{} out".format(fora))
