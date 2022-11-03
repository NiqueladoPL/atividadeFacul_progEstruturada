# Considere os custos dos insumos necessários para produzir um item: Insumo A: 300 reais; Insumo B: 1500 reais; Insumo C: 600 reais; Insumo D: 1000 reais; Insumo E: 150 reais; Insumo F: 225 reais. Sabendo que o insumo F é sempre utilizado, faça um programa que leia a quantidade necessária de cada um dos insumos de A a E e informe o custo final do produto.

qtdInsumosA = int(input("Quantidade do insumo A: "))
qtdInsumosB = int(input("Quantidade do insumo B: "))
qtdInsumosC = int(input("Quantidade do insumo C: "))
qtdInsumosD = int(input("Quantidade do insumo D: "))
qtdInsumosE = int(input("Quantidade do insumo E: "))

custoTotal = ((qtdInsumosA * 300) + (qtdInsumosB * 1500) +
              (qtdInsumosC * 600) + (qtdInsumosD * 1000) + (qtdInsumosE * 150) + 225)

print("R$ {:.2f}".format(custoTotal))