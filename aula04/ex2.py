# Aula 04 - Exercício de fixação 02

qtdProdutos = int(input("Quantidade de produtos: "))
qtdSupVeic = int(input("Quantidade suportada por veículo: "))
qtdVeicDisp = int(input("Qtd veículos disponíveis: "))

qtdVeiculosNeed = qtdProdutos / qtdSupVeic
qtdVeiculosNeed = int(qtdVeiculosNeed)

if qtdVeiculosNeed > qtdVeicDisp:
    print("Não há veículos suficientes")
else:
    print("Transporte Disponível")
