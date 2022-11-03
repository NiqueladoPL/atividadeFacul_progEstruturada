# Um Posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes. Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma: 1.Álcool 2.Gasolina 3.Diesel 4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código (até que seja válido). O programa será encerrado quando o código informado for o número 4.

loop = 1
alcool = 0
gasolina = 0
diesel = 0

while loop > 0:
    cod = int(input("Código: "))
    if (cod == 1):
        alcool = alcool + 1
    elif cod == 2:
        gasolina = gasolina + 1
    elif cod == 3:
        diesel = diesel + 1
    elif cod == 4:
        loop = 0
    elif cod > 4:
        print("Digite um código de 1 a 4")

print("Alcool: "+str(alcool))
print("Gasolina: "+str(gasolina))
print("Diesel: "+str(diesel))
