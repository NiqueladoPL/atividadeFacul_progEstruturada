# a) Leia o nome do(a) vendedor(a);
# b) Leia o valor do salário base desse(a) vendedor(a);
# c) Leia o valor total de produtos vendidos por esse(a) vendedor(a);
# d) Calcule o bônus que ele(a) receberá pelas vendas realizadas (5% do valor total de vendas);
# e) Calcule o salário bruto do(a) vendedor(a) (salário base + bônus);
# f) Calcule o imposto que ele(a) deve pagar ao governo (de acordo com a tabela abaixo);
# g) Apresente o nome do vendedor seguido de seu salário líquido ( salário bruto - impostos).

from calendar import c


nome = input("Digite o nome do(a) vendedor(a): ")
salBase = float(input("Digite o salário base: "))
totalVendido = float(input("Digite o valor total de vendas: "))

bonus = (totalVendido/100) * 5

salBruto = salBase + bonus

if salBruto < 1903.99:
    imposto = 0
elif (salBruto >= 1903.99) and (salBruto < 2826.66):
    imposto = ((salBruto / 100) * 7.5)
elif (salBruto >= 2826.66) and (salBruto < 3751.05):
    imposto = ((salBruto / 100) * 15)
elif (salBruto >= 3751.06) and (salBruto <= 4664.68):
    imposto = ((salBruto / 100) * 22.5)
elif salBruto > 4664.68:
    imposto = ((salBruto / 100) * 27.5)

salLiquido = salBruto - imposto

print("{} : R$ {:.2f}".format(nome, salLiquido))
