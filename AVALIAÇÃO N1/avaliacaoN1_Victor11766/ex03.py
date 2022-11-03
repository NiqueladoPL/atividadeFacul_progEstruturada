# 3. Uma indústria usa três insumos na produção de caixas de papelão biodegradáveis: algodão em farelo, biomassa de babosa e celulose. Sabendo que o custo máximo a ser gasto de insumo em uma unidade de caixa de papelão é de R$ 2,00, desenvolva um programa que:
# a. Leia os custos dos insumos algodão em farelo e biomassa de babosa por caixa;
# b. Calcule o custo máximo que pode ser gasto de celulose por caixa;
# c. Informe qual dos insumos tem o preço mais alto.

custoAlgodao = float(input("Custo com algodão em farelo: "))
custoBiomassa = float(input("Custo com biomassa de babosa: "))

maxCelulose = (2 - (custoAlgodao + custoBiomassa))

maisCaro = custoAlgodao

if custoBiomassa > maisCaro:
    msgCaro = "Biomassa de Barbosa"
elif maxCelulose > maisCaro:
    msgCaro = "Celulose"
else:
    msgCaro = "Algodão em Farelo"

print("Insumo mais caro: {}".format(msgCaro))
