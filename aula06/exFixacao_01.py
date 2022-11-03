# Faça um programa que leia uma série de números e informe quantos deles são positivos e quantos são negativos. Inicialmente são informados a quantidade de números a serem verificados e em seguida são informados os números.

qtdNum = int(input("Quantidade de números: "))
print("Insira os núemros separados por espaço, ex:(45 12 -8 21)")
numeros = input("-> ")
numSplit = numeros.split()
tamanhoSplit = len(numSplit)

acc = 0
positivo = 0
negativo = 0

if (tamanhoSplit < qtdNum) or (tamanhoSplit > qtdNum):
    print("Quantidade inserida diferente da informada!")
else:
    while acc < qtdNum:
        x = float(numeros.split()[acc])
        if x >= 0:
            positivo = positivo + 1
        else:
            negativo = negativo + 1
        acc = (acc + 1)

print("Positivos: {}".format(positivo))
print("Negativos: {}".format(negativo))
