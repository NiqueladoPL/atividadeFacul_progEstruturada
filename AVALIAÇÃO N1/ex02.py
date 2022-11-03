# Uma determinada quantidade de material é necessário para produzir uma peça específica.
# Dado a quantidade total de material disponível, a quantidade de material necessário para produzir uma peça e a quantidade de peças necessárias, calcule e informe “Quantidade suficiente” se a quantidade de material seja o bastante para produzir as peças necessárias, ou “Quantidade insuficiente”, caso contrário.

qtdTotalMaterial = int(input("Quantidade total de material: "))
qtdMaterialPeca = int(input("Quantidade de material por peça: "))
qtdPecasNecessarias = int(input("Quantidade de peças necessárias: "))

materialNecessario = (qtdMaterialPeca * qtdPecasNecessarias)

if materialNecessario > qtdTotalMaterial:
    print("Quantidade insuficiente")
else:
    print("Quantidade suficiente")
