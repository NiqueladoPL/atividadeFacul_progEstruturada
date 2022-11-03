import math
from unittest import result

largura, comprimento, porcentagem = (
    input("Largura Comprimento Porcentagem: ")).split(" ")

largura = int(largura)
comprimento = int(comprimento)
porcentagem = int(porcentagem)/100

resultado = math.sqrt((largura * comprimento) / porcentagem)

print(resultado)
