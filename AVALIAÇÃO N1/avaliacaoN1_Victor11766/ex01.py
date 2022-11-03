# O principal cliente de uma determinada indústria precisa de um determinado número de peças.
# Dado o tempo necessário para produzir uma peça em minutos e a quantidade de peças necessárias, calcule e informe o tempo necessário para produzir todas as peças em minutos.

tempoProducao = int(input("Tempo necessário para produzir uma peça: "))
qtdPecas = int(input("Quantidade de peças necessárias: "))

tempoNecessario = (tempoProducao * qtdPecas)

print("Tempo necessário para produzir: {}".format(tempoNecessario))
