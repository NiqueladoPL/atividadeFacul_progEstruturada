# Sabendo que um caixa eletrônico tem um total de 10 notas de cada uma das células (100, 50, 20, 10, 5 e 2) Faça um sistema para informar se é possível fazer um determinado saque ou não.
# a. Leia o valor para realizar o saque;
# b. Calcule a menor quantidade de notas necessárias;
# c. Leia o valor a ser sacado;
# d. Exiba “Saque possível” caso seja possível fazer o saque ou “Saque impossível” caso não seja.
# e. No final, se o saque foi possível, exiba quantas notas restaram.

valorSaque = float(input("Valor para sacar: "))

if (valorSaque < 2) or (valorSaque > 1870):
    print("Saque Impossível")
else:
    print("Saque Possível")
    n100 = int(valorSaque / 100)
    tot100 = (10 - n100)
    print("Notas restantes:")
    print("Notas de R$ 100,00: {}".format(tot100))

    valorSaque = (valorSaque - (100 * n100))
    n50 = int(valorSaque / 50)
    tot50 = (10 - n50)
    print("Notas de R$ 50,00: {}".format(tot50))

    valorSaque = (valorSaque - (50 * n50))
    n20 = int(valorSaque / 20)
    tot20 = (10 - n20)
    print("Notas de R$20,00: {}".format(tot20))

    valorSaque = (valorSaque - (20 * n20))
    n10 = int(valorSaque / 10)
    tot10 = (10 - n10)
    print("Notas de R$10,00: {}".format(tot10))

    valorSaque = (valorSaque - (10 * n10))
    n5 = int(valorSaque / 5)
    tot5 = (10 - n5)
    print("Notas de R$5,00: {}".format(tot5))

    valorSaque = (valorSaque - (5 * n5))
    n2 = int(valorSaque / 2)
    tot2 = (10 - n2)
    print("Notas de R$2,00: {}".format(tot2))
